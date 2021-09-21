from rest_framework import viewsets
from .serializers import imageSerializer
from .models import image
from django.http import JsonResponse
from rest_framework.response import Response
from tensorflow.keras.models import load_model
import cv2
import numpy
import uuid
import numpy as np
import pandas as pd
from django.conf import settings
import os
import json

def imageHash(image, size=8):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (size + 1, size))

    diff = img[:, 1:] > img[:, :-1]
    diff = diff.flatten().astype(int)
    return "".join(str(x) for x in diff)


def hammingDistance(n1, n2):
    n1 = int(n1, 2)
    n2 = int(n2, 2)
    x = n1 ^ n2
    setBits = 0
    while (x > 0):
        setBits += x & 1
        x >>= 1
    return setBits

class imageViewSet(viewsets.ModelViewSet):
    queryset = image.objects.all().order_by('created').reverse()
    serializer_class = imageSerializer

    def classifyContent(self, img):

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (200, 200))
        img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        testData = np.array([img])
        testData = np.array([x.reshape(200, 200, 1) for x in testData])

        model = load_model(os.path.join(settings.BASE_DIR, 'imageRepo/classifierScripts/models/model1_10000_literer'))
        predictions = model.predict(testData)

        data = pd.read_csv(os.path.join(settings.BASE_DIR, 'imageRepo/classifierScripts/data/classMappingLiterer.csv'))
        classes = []
        for i in range(len(predictions[0])):
            if (predictions[0][i] > 0.45):
                classes.append(data['Word'][i])
        return classes

    def list(self, request, *args, **kwargs):
        self.queryset = image.objects.all().order_by('created').reverse()
        contentFilters = json.loads(request.GET.get('content', '[]'))

        if len(contentFilters) > 0:
            filtered = []
            for i in self.queryset:
                content = i.content
                if('content' in content):
                    if bool(set(content['content']) & set(contentFilters)):
                        filtered.append(self.serializer_class(i).data)
            return Response(filtered)
        else:
            return Response([self.serializer_class(i).data for i in self.queryset])

    def create(self, request, *args, **kwargs):
        img = request.FILES['main_image']
        decodedImg = cv2.imdecode(numpy.fromstring(img.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)

        content = self.classifyContent(decodedImg);

        image.objects.create(
            id=str(uuid.uuid4()), title=request.POST['title'], hash=imageHash(decodedImg), main_image=img, width=decodedImg.shape[1], height=decodedImg.shape[0], content={'content':content})
        return JsonResponse({'result':'ok'})

class imageSearchViewSet(viewsets.ModelViewSet):
    queryset = image.objects.all().order_by('created').reverse()
    serializer_class = imageSerializer

    def create(self, request, *args, **kwargs):
        self.queryset = image.objects.all().order_by('created').reverse()
        img = cv2.imdecode(numpy.fromstring(request.FILES['main_image'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        hash = imageHash(img)
        hits = []
        for i in self.queryset:
            if(hammingDistance(hash, i.hash) <= 10):
                hits.append(self.serializer_class(i).data)

        return Response(hits)


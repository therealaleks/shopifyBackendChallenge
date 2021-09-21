from django.db import models
from datetime import datetime

class image(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    title = models.CharField(max_length=200)
    hash = models.TextField(max_length=64)
    main_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now)
    content = models.JSONField(default=dict)

    def __str__(self):
        return self.title
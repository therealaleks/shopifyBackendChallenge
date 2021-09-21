# Generated by Django 3.2.7 on 2021-09-21 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('hash', models.TextField(max_length=64)),
                ('main_image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.JSONField(default=dict)),
            ],
        ),
    ]

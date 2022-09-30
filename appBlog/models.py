from datetime import date
from distutils.command.upload import upload
from django import urls
from django.db import models

# Create your models here.

class Post (models.Model):
    title= models.CharField(max_length=400)
    description= models.TextField(max_length=1000)
    date_post= models.DateField(auto_now=True)
    image= models.ImageField(upload_to= 'public/')
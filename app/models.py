from django.db import models
from django.http import HttpResponse


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=25,primary_key=True)
class webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,primary_key=True)
    url = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
class Access_Record(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)

from django.db import models
from django.contrib.postgres.fields import ArrayField

class homepagedata(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    about_headline = models.CharField(max_length=200)
    about_headline_description = models.CharField(max_length=400)
    social_links = ArrayField(
        models.URLField(),  
        null=True )         

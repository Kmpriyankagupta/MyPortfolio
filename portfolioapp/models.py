from django.db import models
from django.contrib.postgres.fields import ArrayField

class homepagedata(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    about_headline = models.CharField(max_length=200)
    about_headline_description = models.CharField(max_length=400)
    about_headline_description1 = models.CharField(max_length=40)
    text_array = ArrayField(
        models.TextField(),  # Specifies the type of the array (TextField in this case)
        blank=True,           # Allows the field to be empty in forms (doesn't require input)
        null=True,            # Allows the field to store NULL values in the database
        default=list         # Default to an empty list if no value is provided
    )
    clients_heading = models.CharField(max_length=200)
    clients_description = models.CharField(max_length=400)
    clients_description1 = models.CharField(max_length=40)
    exerpertise = models.CharField(max_length=200)
    exerpertise_description = models.CharField(max_length=400) 
    expse_type1_heading = models.CharField(max_length=200)
    expse_type1_description = models.CharField(max_length=400) 
    expse_type2_heading = models.CharField(max_length=200)
    expse_type2_description = models.CharField(max_length=400) 
    expse_type3_heading = models.CharField(max_length=200)
    expse_type3_description = models.CharField(max_length=400) 
    expse_type4_heading = models.CharField(max_length=200)
    expse_type4_description = models.CharField(max_length=400) 
    
    def __str__(self):
        return self.name

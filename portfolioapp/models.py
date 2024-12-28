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
        models.TextField(),  
        blank=True,           
        null=True,            
        default=list        
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
    
    
class aboutpagedata(models.Model):
    description = models.CharField(max_length=50)
    inspire_heading = models.CharField(max_length=150)
    inspire_description= models.CharField(max_length=1000)
    about_image = models.ImageField(upload_to='profile_about/', null=True, blank=True)
    inspire_description= models.CharField(max_length=1000)
    got_heading= models.CharField(max_length=100)
    got_description= models.CharField(max_length=1000)
    values_heading= models.CharField(max_length=100)
    value_subheading1 =models.CharField(max_length=100)
    value_description1= models.CharField(max_length=1000)
    value_subheading2 =models.CharField(max_length=100)
    value_description2= models.CharField(max_length=1000)
    value_subheading3 =models.CharField(max_length=100)
    value_description3= models.CharField(max_length=1000)
    value_subheading4 =models.CharField(max_length=100)
    value_description4= models.CharField(max_length=1000)
    work_heading =models.CharField(max_length=100)
    work_description= models.CharField(max_length=1000)
    work_description1= models.CharField(max_length=1000)
    morewords_heading =models.CharField(max_length=100)
    morewords_description= models.CharField(max_length=1000)
    def __str__(self):
        return self.description
    
class contact(models.Model):
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    tutle_des = models.CharField(max_length=1000)
    toge_heading = models.CharField(max_length=1000)
    toge_des = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.BigIntegerField()
    def __str__(self):
        return self.description
    
    
# class servicepagedata(models.Model):
#     description = models.CharField(max_length=50)
#     impact_heading = models.CharField(max_length=150)
#     impact_description= models.CharField(max_length=1000)
#     about_image = models.ImageField(upload_to='profile_about/', null=True, blank=True)
#     inspire_description= models.CharField(max_length=1000)
#     got_heading= models.CharField(max_length=100)
#     got_description= models.CharField(max_length=1000)
#     values_heading= models.CharField(max_length=100)
#     value_subheading1 =models.CharField(max_length=100)
#     value_description1= models.CharField(max_length=1000)
#     value_subheading2 =models.CharField(max_length=100)
#     value_description2= models.CharField(max_length=1000)
#     value_subheading3 =models.CharField(max_length=100)
#     value_description3= models.CharField(max_length=1000)
#     value_subheading4 =models.CharField(max_length=100)
#     value_description4= models.CharField(max_length=1000)
#     work_heading =models.CharField(max_length=100)
#     work_description= models.CharField(max_length=1000)
#     work_description1= models.CharField(max_length=1000)
#     morewords_heading =models.CharField(max_length=100)
#     morewords_description= models.CharField(max_length=1000)
#     def __str__(self):
#         return self.description

    
    

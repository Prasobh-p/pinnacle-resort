from django.db import models

# Create your models here.
class Accomdb(models.Model):
    NAME = models.CharField(max_length=50,null=True,blank=True)
    IMAGE = models.FileField(upload_to='images', null=True, blank=True)
    DESCRIPTION = models.CharField(max_length=1000, null=True, blank=True)


class Roomdb(models.Model):
    ROOMTYPE = models.CharField(max_length=50,null=True,blank=True)
    NAME = models.CharField(max_length=50,null=True,blank=True)
    PRICE = models.IntegerField(null=True,blank=True)
    IMAGE = models.FileField(upload_to='images', null=True, blank=True)
    BEDDING = models.CharField(max_length=50,null=True,blank=True)
    AMENITIES = models.CharField(max_length=500,null=True,blank=True)
    VIEWS = models.CharField(max_length=50,null=True,blank=True)
    POOL= models.CharField(max_length=50,null=True,blank=True)



class Fooddb(models.Model):
    FNAME = models.CharField(max_length=50,null=True,blank=True)
    FIMAGE = models.FileField(upload_to='images', null=True, blank=True)
    FDESCRIPTION = models.CharField(max_length=1000, null=True, blank=True)



class Fooditeamsdb(models.Model):
    FOODTYPE = models.CharField(max_length=50,null=True,blank=True)
    FONAME = models.CharField(max_length=50,null=True,blank=True)
    FOPRICE = models.IntegerField(null=True,blank=True)
    FOIMAGE=models.FileField(upload_to='images', null=True, blank=True)
    FODESCRIPTION = models.CharField(max_length=50,null=True,blank=True)










from django.db import models
from backend.models import Roomdb

# Create your models here.
class Condb(models.Model):
    NAME = models.CharField(max_length=50,blank=True,null=True)
    SUBJECT = models.CharField(max_length=50,blank=True,null=True)
    MESSAGE = models.TextField(max_length=100,blank=True,null=True)
    EMAIL = models.EmailField(max_length=250, blank=True, null=True)


class Registerdb(models.Model):
    Name = models.CharField(max_length=500,blank=True,null=True)
    Email = models.EmailField(max_length=500,blank=True,null=True)
    Password = models.CharField(max_length=500,blank=True,null=True)
    ConfirmPassword = models.CharField(max_length=500, blank=True, null=True)




class Hostdb(models.Model):
    roomname = models.CharField(max_length=500, null=True, blank=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    customers = models.PositiveIntegerField()
    total_price=models.CharField(max_length=500,null=True,blank=True)



class Paymentdb(models.Model):
    Hostname=models.CharField(max_length=500,null=True,blank=True)
    Mobnum = models.CharField(max_length=100, null=True, blank=True)
    Paymail=models.EmailField(max_length=1000,null=True,blank=True)
    Proof = models.FileField(upload_to="images", null=True, blank=True)
    Address = models.CharField(max_length=1000, null=True, blank=True)
    Requerments = models.CharField(max_length=1000, null=True, blank=True)
    Originaltotal_price = models.CharField(max_length=500, null=True, blank=True)








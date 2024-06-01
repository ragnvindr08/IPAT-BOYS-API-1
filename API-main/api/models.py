from django.db import models

# Create your models here.

class Item(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100, default="")
    middlename = models.CharField(max_length=100, null=True)  # middlename can be null
    address = models.CharField(max_length=255, null=True)  # address can be null
    birthday = models.DateField(null=True)  # birthday can be null
    phone_no = models.CharField(max_length=15, null=True)  # phone_no can be null
    created = models.DateTimeField(auto_now_add=True)
   
 

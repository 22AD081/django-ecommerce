from django.db import models
from django.contrib.auth.models import User
class Account_details(models.Model):
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=255,null=True)
    password=models.CharField(max_length=10,null=True)
    phoneno=models.CharField(max_length=20,null=True)
class Products(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=30,null=True)
    price= models.DecimalField(max_digits=10,decimal_places=2,null=True)
class Accessory(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=30,null=True)
    price= models.DecimalField(max_digits=10,decimal_places=2,null=True)
class Brand(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=30,null=True)
    desc=models.CharField(max_length=100,null=True)
class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.

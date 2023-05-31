from django.db import models

# Create your models here.
class test(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    price=models.IntegerField(null=False)
    desc=models.CharField(max_length=100,null=False)

class accounts(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    contact=models.IntegerField(null=True)
    gender=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=100,null=True)


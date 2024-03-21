from django.db import models

from .managers import ProductManager
from autoslug import AutoSlugField
# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=12)
    slug=AutoSlugField(populate_from="category_name")

    def __str__(self):
        return self.category_name



class product(models.Model):
    pro_name=models.CharField(max_length=50,default="ProductName")
    pro_desc=models.TextField(default="description")
    pro_Price=models.IntegerField(default=0)
    pro_Brand=models.CharField(max_length=75,default="paws")
    pro_picture=models.ImageField(upload_to="images/",default="")
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    pm=models.Manager() #pm=productmana
    cm=ProductManager() #cm=custommanager

    def __str__(self):
        return self.pro_name
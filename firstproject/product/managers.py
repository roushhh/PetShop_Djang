from django.db import models
from django.db.models.query import QuerySet

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model)
        

    def sorted(self):
        return super().get_queryset().order_by('pro_name')
    
    def catproduct(self):
        return super().get_queryset().filter(pro_name__icontains="cat")

    def sortByPrice(self):
        return super().get_queryset().order_by('pro_Price')

class ProductQuerySet(models.QuerySet):
     
     def getPawsIndia(self):
         return self.filter(pro_Brand="pawsUp")
     
























     
         
        
         
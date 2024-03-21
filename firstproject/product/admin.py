from django.contrib import admin
from .models import product,Category

# Register your models here.



@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','pro_name','pro_desc','pro_Price','pro_Brand','pro_picture','Category')


#Registering category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')


#admin.site.register(product,ProductAdmin)    
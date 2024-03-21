from django.contrib import admin
from django.urls import path
from .views import ProductView,productdetailview,field_lookup,CategoryDetailViews

urlpatterns = [

    path('product/',ProductView.as_view()),
    path('product/<int:pk>',productdetailview.as_view(),name="productdetail"), #productdetail"
    path('productlookup/',field_lookup),
    path('category/<slug:slug>',CategoryDetailViews.as_view(),name="category")
]



# <h1 class="h1"> <a href="{% url 'homepage'%}"> PRODUCT List </a> </h1>

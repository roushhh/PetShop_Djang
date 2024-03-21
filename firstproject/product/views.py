from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic  import DetailView
from .models import product,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url="/login/"),name="dispatch")
class ProductView(ListView):
    model=product
    template_name="products.html"


class productdetailview(DetailView):
    model=product
    template_name="product_detail.html"
    context_object_name="p"


def field_lookup(request):
   products=product.pm.all()
   # products=product.cm.all().filter(Q(id=10)& Q(pro_name__icontains="DOG"))
   #products=product.cm.all().filter(Q(pro___lt=500)& Q(pro_name__icontains="DOG"))
   #products=product.pm.all().filter( pro_Brand="pawsup")
   #products=product.objects.filter(pro_Price__lte="600")
   #products=product.objects.filter(pro_Price__gte="600")
   #products=product.objects.filter(pro_name__contains="dog") #case sensitve
   #products=product.objects.filter(pro_name__icontains="dog") #case sensitve
   #products=product.objects.filter(pro_Brand__istartswith="P") #case sensitve
   #products=product.objects.filter(pro_name__iendswith="p") #case sensitve
   #products=product.objects.filter(id__in=[2,3,4,5]) 
 



   return render(request,"productlookup.html",{"product":products})


class CategoryDetailViews(DetailView):
    model=Category
    template_name="category.html"
    content_type_name="category"
    slug_field="slug"
import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from product.models import product
from .models import Order, OrderItem, cart,CartItem

# Create your views here.


def add_to_cart(request,productId):
    #Logic for Adding cart

    products=get_object_or_404(product,id=productId)
    print(products.pro_name)

    #Fetching current User
    currentuser=request.user

    carts,created=cart.objects.get_or_create(user=currentuser)

    print(created)

    item,item_created= CartItem.objects.get_or_create(cart=carts,products=products)

    quantity=request.GET.get("quantity")

    if not item_created:
        item.quantity+=int(quantity)
    else:
        item.quantity=1

    item.save()        

    return HttpResponseRedirect("/pro/productlookup/")

                    #views cart 

def view_cart(request):
    currentUser=request.user
    carts,created=cart.objects.get_or_create(user=currentUser)
    CartItems=carts.cartitem_set.all()
    print(CartItems)
    finalAmount=0

    for item in CartItems:
        finalAmount+=item.quantity*item.products.pro_Price



    return render(request,"cart.html",{"items":CartItems,"finalAmount":finalAmount})


    #UpdateCart

def update_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    quantity=request.GET.get("quantity")
    print(quantity)
    cartItem.quantity=int(quantity)
    cartItem.save()
    return HttpResponseRedirect("/cart/")


   #Delete Cart Item

def delete_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    cartItem.delete()
    return HttpResponseRedirect("/cart/")


from .forms import OrderForm

def check_out(request):
     currentUser=request.user
     initial={
        "user":currentUser.get_username(),
        "first_name":currentUser.get_short_name(),
        "last_name":currentUser.last_name
    }
     
    
 

     form=OrderForm(initial=initial)
     currentUser=request.user
     carts,created=cart.objects.get_or_create(user=currentUser)
     CartItems=carts.cartitem_set.all()
     print(CartItems)
     finalAmount=0
     

     for item in CartItems:
        finalAmount+=item.quantity*item.products.pro_Price
     if request.method=="POST":
          form=OrderForm(request.POST)
          if form.is_valid():
                           user=request.user
                           first_name=form.cleaned_data['first_name']
                           last_name=form.cleaned_data['last_name']
                           address=form.cleaned_data['address']
                           city=form.cleaned_data['city']
                           state=form.cleaned_data['state']
                           pincode=form.cleaned_data['pincode']
                           phoneno=form.cleaned_data['phoneno']
                           orderId=str(uuid.uuid4())



                           order=Order.objects.create(user=user,first_name=first_name,last_name=last_name,
                                 address=address,city=city,state=state,pincode=pincode,phoneno=phoneno,order_id=orderId[:8])
                           for item in CartItems:
                                OrderItem.objects.create(
                                        order=order,
                                        products=item.products,
                                     quantity=item.quantity,
                                    total=item.quantity*item.products.pro_Price
                               )



          return HttpResponseRedirect("/payment/"+orderId[:8])

     return render(request,"checkout.html",{"form":form,"items":CartItems,"finalAmount":finalAmount})
 



import razorpay

def MakePayment(request,orderId):
    print(orderId)
    orders=Order.objects.get(pk=orderId)
    orderItem=orders.orderitem_set.all()
    amount=0

    for item in orderItem:
        amount+=item.total


    client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))
    data = { "amount": amount*100   , "currency": "INR", "receipt": orderId,"payment_capture":1 }
    payment = client.order.create(data=data)   

    return render(request,"payment.html",{"payment":payment})



# Success Page
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@csrf_exempt
def success(request,orderId):
    if request.method=="POST":
         client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))
         check=client.utility.verify_payment_signature({
                         'razorpay_order_id': request.POST.get("razorpay_order_id"),
                         'razorpay_payment_id':request.POST.get  ("razorpay_payment_id"),
                          'razorpay_signature': request.POST.get ("razorpay_signature")
   })
         if check:
              order=Order.objects.get(pk=orderId)
              order.paid=True
              order.save()
              carts=cart.objects.get(user=request.user)
              OrderItem=order.orderitem_set.all()
              carts.delete()
              send_mail(
                   "Order Placed...",
                   "",#Message
                    settings.EMAIL_HOST_USER,
                   ["roushanshaikh040403@gmail.com"],
                   fail_silently=False,
                   html_message=render_to_string("email.html",{"items":OrderItem})
                   


              )
    


    return render(request,"success.html",{})
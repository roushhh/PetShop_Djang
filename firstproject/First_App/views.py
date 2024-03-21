from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")



def firstpage(request):
    return HttpResponse("<h1>first page</h1>")


def about(request):
    return HttpResponse("About Us")

def users(request):
    student={ 
        "id":101,
        "name":"roushan",
        "age":18
         }
    return render(request,"index.html",student)

def pages(request):
    student={
        "id":102,
        "name":"jari",
        "age":20

    }
    return render(request,"class.html")



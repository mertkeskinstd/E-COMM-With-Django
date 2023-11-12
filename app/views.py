from urllib import request

from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from django.db.models import Count
from app import models
from .models import Product
from .forms import CustomRegistrattionForm


# Create your views here.

app_name='app'


def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")


class CategoryVievs(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values("title")
        return render(request,"app/category.html",locals())
    
class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationForm(View):
    def get(self,request):
        form=CustomRegistrattionForm()
        return render(request,'app/userlogin.html',locals())
    
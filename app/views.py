from urllib import request
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.db.models import Count
from app import models
from .models import Product,Customer,Cart,Wishlist
from .forms import CustomRegistrattionForm,CustomProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

app_name='app'

@login_required
def home(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/home.html")

@login_required
def about(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())

@login_required
def contact(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/contact.html",locals())

method_decorator(login_required,name="dispatch")
class CategoryVievs(View):
    def get(self,request,val):
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

method_decorator(login_required,name="dispatch")
class CategoryTitle(View):
    def get(self,request,val):
        
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values("title")
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/category.html",locals())
    
method_decorator(login_required,name="dispatch")
class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        
        wishlist=Wishlist.objects.filter(Q(product=product)& Q(user=request.user))
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail.html",locals())
    
method_decorator(login_required,name="dispatch")
class CustomerRegistrationForm(View):
    def get(self,request):
        form=CustomRegistrattionForm()
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request,'app/userlogin.html',locals())
    def post(self,request):
        form=CustomRegistrattionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/userlogin.html',locals())
        

method_decorator(login_required,name="dispatch")
class ProfileView(View):
    def get(self,request):
        form=CustomProfileForm()
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form=CustomProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            
            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/profile.html',locals())

@login_required  
def address(request):
    add=Customer.objects.filter(user=request.user)
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/address.html',locals())

method_decorator(login_required,name="dispatch")
class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomProfileForm(instance=add)
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form=CustomProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')
    
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    # Aynı kullanıcı ve ürün ile bir sepet öğesi var mı diye kontrol et
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)

    if not created:
        # Öğe zaten varsa, miktarı arttır
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart')

@login_required
def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.discounted_price
        amount=amount + value
    totalamount=amount+40
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/addtocart.html',locals())

@login_required
def show_wishlist(request):
    user=request.user
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    product=Wishlist.objects.filter(user=user)
    return render(request,"app/wishlist.html",locals())
        

method_decorator(login_required,name="dispatch")
class checkout(View):
    def get(self,request):
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famout=0
        for p in cart_items:
            value=p.quantity * p.product.discounted_price
            famout=famout + value
        totalamount=famout +40
        return render(request,'app/checkout.html',locals())

def pluscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.discounted_price
            amount=amount + value
        totalamount=amount+40
        data={
            "quantity":c.quantity,
            "amount":amount,
            "totalamount":totalamount
        }
        return JsonResponse(data)

def minuscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.discounted_price
            amount=amount + value
        totalamount=amount+40
        data={
            "quantity":c.quantity,
            "amount":amount,
            "totalamount":totalamount
        }
        return JsonResponse(data)
    
def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        
        # Filtre kullanarak aynı ürünü içeren tüm Cart nesnelerini al
        carts = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
        
        # Tüm Cart nesnelerini silebilirsiniz
        carts.delete()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            "amount": amount,
            "totalamount": totalamount
        }
        return JsonResponse(data)




def pluswishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist Added Successfully'
        }
        
        return JsonResponse(data)

def minuswishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)


@login_required
def search(request):
    query=request.GET['search']
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    product=Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())

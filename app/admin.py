from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlace,Wishlist
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group
# Register your models here.


@admin.register(Product)
class productmodeladmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']
    



@admin.register(Customer)
class Customermodeladmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']
    


@admin.register(Cart) 
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','products','quantity']
    def products(self,obj):
        link=reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    
    
    
    
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','rezorpay_order_id','rezorpay_payment_status','rezorpay_payment_id','paid']

@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']
    
    
    
    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['id','user','products']
    def products(self,obj):
        link=reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    
    
admin.site.unregister(Group)
    
    

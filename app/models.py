
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

STATE_CHOICES = (
    ("Baden-Wurttemberg", "Baden-Wurttemberg"),
    ("Bavaria", "Bavaria"),
    ("Berlin", "Berlin"),
    ("Brandenburg", "Brandenburg"),
    ("Bremen", "Bremen"),
    ("Hamburg", "Hamburg"),
    ("Hesse", "Hesse"),
    ("Lower Saxony", "Lower Saxony"),
    ("Mecklenburg-Vorpommern", "Mecklenburg-Vorpommern"),
    ("North Rhine-Westphalia", "North Rhine-Westphalia"),
    ("Rhineland-Palatinate", "Rhineland-Palatinate"),
    ("Saarland", "Saarland"),
    ("Saxony", "Saxony"),
    ("Saxony-Anhalt", "Saxony-Anhalt"),
    ("Schleswig-Holstein", "Schleswig-Holstein"),
    ("Thuringia", "Thuringia")
)

CATEGORY_CHOICES=(
    ('CR','Curd'),
        ('ML','Milk'),
            ('LS','Lassi'),
                ('MS','Milkshake'),
                    ('PN','Panner'),
                        ('GH','Ghee'),
                            ('CZ','Cheese'),
                                ('IC','Ice-Creams'),    
)




class Product(models.Model):
    
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    
    def __str__(self) -> str:
        return self.title
    






class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self) :
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
    
)

    
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    rezorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    rezorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    rezorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)

class OrderPlace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="Pending")
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity *self.product.discounted_price
    


    
class Wishlist(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
   
    
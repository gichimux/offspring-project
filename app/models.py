from django.db import models
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from postgres_copy import CopyManager

'''
Class category for product categories
'''
class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    def save_tag(self):
        self.save()
    def __str__(self):
        return self.name
'''
class product for product in general stock
'''
class Product(models.Model):
    name = models.CharField(max_length= 50,blank=False,null= False)
    sKU = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    product_color = models.CharField(max_length=50,blank=False)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    unit_tax = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=50,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name + '-'+ self.sKU

'''
class distributor for the different product distributors
'''

class Distributor(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30,default="karen")
    def __str__(self):
        return self.location


class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    warehouse=models.ForeignKey(Distributor,on_delete=models.CASCADE,blank=False,null=False)
    quantity =models.PositiveIntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    time=models.DateTimeField(null=True)
    month=models.PositiveIntegerField(default=0)
    year=models.PositiveIntegerField(default=0)
  
    
    def __str__(self):
        return self.product.name

    @classmethod
    def search_by_id(cls,search_id):
        product=cls.objects.filter(order_id__icontains=search_id)
        return 

    def year(self):
        return self.date.strftime('%Y')
    
    

'''
class House_product for the products in particular house
'''

class House_Product(models.Model):
    name = models.ForeignKey(Product,blank=False,null=False,related_name="location")
    sKU = models.CharField(max_length= 10,default='I')
    category = models.ForeignKey(Category,default='Toys')
    warehouse = models.ForeignKey('Distributor',default=1,related_name="warehouse_products")
    quantity =models.PositiveIntegerField(default=0)
    
    @classmethod
    def search_by_serial(cls,search_serial):
        products=cls.objects.filter(serial__icontains=search_serial)
        return products

    def __str__(self):
        return self.name.name + '-' + self.sKU

'''
class for the product suppliers
'''

class Supplier(models.Model):
    name = models.CharField(max_length= 50)
    product = models.CharField(max_length= 50)
    contact = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name

'''
class order product that stores details of product
being updated to stock from supplier 
'''

class Order_Product(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    supplier=models.ForeignKey(Supplier,blank=True,null=True)
    quantity =models.PositiveIntegerField(default=0)
    month= models.PositiveIntegerField(default=0)
    
    year= models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name 
    def year(self):
        return self.date.strftime('%Y')

    def month(self):
        return self.date.strftime('%m')


'''
class to update items quantity when sold by a specific
distributor
'''

class Customer_order(models.Model):
    product=models.ForeignKey(House_Product,on_delete=models.CASCADE,blank=False,null=False,related_name="orders")
    order_serial = models.CharField(max_length= 10)
    sKU = models.CharField(max_length= 10)
    warehouse = models.ForeignKey('Distributor',default=1)
    customer = models.ForeignKey('Customer',default=0)
    quantity =models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    month= models.PositiveIntegerField(default=0)
    year= models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    time=models.DateTimeField(null=True)

    def __str__(self):
        return self.order_serial


class Customer(models.Model):
    name = models.CharField(max_length= 10)
    contact = models.CharField(max_length= 10)
    email = models.CharField(max_length= 30,default='email@example.com')

    def __str__(self):
        return self.name 

class Invoice(models.Model):
    order = models.ForeignKey('Customer_order',default='000')
    date = models.DateTimeField(auto_now=True)

   
class Sales(models.Model):
    item_name=models.CharField(max_length= 20)
    date_sold = models.DateField(auto_now=False)
    predicted=models.IntegerField(default=0)

class Prediction(models.Model):
    item_name=models.CharField(max_length= 20)
    date_sold = models.DateField(auto_now=False)
    predicted=models.IntegerField(default=0)
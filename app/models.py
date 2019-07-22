from django.db import models
import datetime as dt
from django.contrib.auth.models import User

'''
    Sub category for the various products in a certain category
'''

class Sub_Category(models.Model):
    name=models.CharField(max_length = 50)
    def __str__(self):
        return self.name

'''
Class category for product categories
'''
class Category(models.Model):
    name = models.CharField(max_length = 30)
    sub_category =models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    
    def save_tag(self):
        self.save()
    def __str__(self):
        return self.name

'''
class distributor for the different product distributors
'''

class Distributor(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30,default="Karen")
    def __str__(self):
        return self.location


'''
class Product for product in general stock
'''
class Product(models.Model):
    name = models.CharField(max_length= 50,blank=False,null= False)
    serial = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    product_color = models.CharField(max_length=50,blank=False)
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=3)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_serial(cls,search_serial):
        products=cls.objects.filter(serial__icontains=search_serial)
        return products
    size = models.CharField(max_length=50,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name

'''
class distributor for the different product distributors
'''

class Distributor(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30,default="karen")
    def __str__(self):
        return self.location

'''
class order details for the details about a certain order
'''
class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    warehouse=models.ForeignKey(Distributor,on_delete=models.CASCADE,blank=False,null=False)
    quantity =models.IntegerField(blank=False,null=False)
    date= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product

    # @classmethod
    # def search_by_id(cls,search_id):
    #     product=cls.objects.filter(order_id__icontains=search_id)
    #     return 

'''
class House_product for the products in particular house
'''

class House_Product(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Distributor',default=1)
    quantity =models.IntegerField(default=0)
    
    @classmethod
    def search_by_serial(cls,search_serial):
        products=cls.objects.filter(serial__icontains=search_serial)
        return products
    def __str__(self):
        return self.name.name
    @classmethod
    def search_by_serial(cls,search_serial):
        products=cls.objects.filter(serial__icontains=search_serial)
        return products

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
    name=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    quantity =models.IntegerField(default=0)
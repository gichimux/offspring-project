from django.db import models
import datetime as dt
from django.contrib.auth.models import User

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
    serial = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    product_color = models.CharField(max_length=50,blank=False)
    quantity = models.IntegerField(default=0)
    size = models.IntegerField(unique= True)
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
        return self.locality

'''
class order details for the details about a certain order
'''
class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    warehouse=models.ForeignKey(Distributor,on_delete=models.CASCADE,blank=False,null=False)
    quantity =models.IntegerField(default=0)
    date= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product

    @classmethod
    def search_by_id(cls,search_id):
        product=cls.objects.filter(order_id__icontains=search_id)
        return 

'''
class House_product for the products in particular house
'''

class House_Product(models.Model):
    name = models.ForeignKey(Product)
    warehouse = models.ForeignKey('Distributor',default=1)
    quantity =models.IntegerField(default=0)
    
    def __str__(self):
        return self.name.name

'''
class for the product suppliers
'''

class Supplier(models.Model):
    name = models.CharField(max_length= 50)
    product = models.CharField(max_length= 50)
    contact = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name


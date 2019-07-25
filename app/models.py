from django.db import models
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator 
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
    sKU = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    product_color = models.CharField(max_length=50,blank=False)
    @classmethod
    def search_by_serial(cls,search_serial):
        products=cls.objects.filter(serial__iexact=search_serial)
    def __str__(self):
        return self.name


class OrderDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    warehouse=models.ForeignKey(Distributor,on_delete=models.CASCADE,blank=False,null=False)

    # @classmethod
    # def search_by_id(cls,search_id):
    #     product=cls.objects.filter(order_id__icontains=search_id)
    #     return 

    def year(self):
    
    

'''
class House_product for the products in particular house
'''

class House_Product(models.Model):
    name = models.ForeignKey(Product)
    sKU = models.CharField(max_length= 10,default='I')
    category = models.ForeignKey(Category,default='Toys')
    warehouse = models.ForeignKey('Distributor',default=1)
    quantity =models.PositiveIntegerField(default=0)
    
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
    Class for the product suppliers
'''

class Supplier(models.Model):
    name = models.CharField(max_length= 50)
    product = models.CharField(max_length= 50)
    contact = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name

'''
    Class order product that stores details of product being updated to stock from supplier 
'''

class Order_Product(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    supplier=models.ForeignKey(Supplier,blank=True,null=True)
    quantity =models.PositiveIntegerField(default=0)
    month= models.PositiveIntegerField(default=0)
    year= models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.product + ''+self.quantity
    def year(self):
        return self.date.strftime('%Y')

    def month(self):
        return self.date.strftime('%m')


'''
class to update items quantity when sold by a specific
distributor
'''

class Distributor_sell(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    sKU = models.CharField(max_length= 10)
    warehouse = models.ForeignKey('Distributor',default=1)
    quantity =models.PositiveIntegerField(default=0)
    month= models.PositiveIntegerField(default=0)
    year= models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.warehouse + ''+self.quantity
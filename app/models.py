from django.db import models


# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length= 50,blank=False,null= False)
    description = models.CharField(max_length=200)
    prod_color = models.CharField(max_length=50,blank=False)
    prod_id = models.AutoField(primary_key=True)  
    quantity = models.IntegerField(default=0)
    size = models.IntegerField(unique= True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name

class Warehouse(models.Model):
    locality=models.CharField(max_length=100,default='Karen')
    def __str__(self):
        return self.locality

class OrderDetails(models.Model):
    order_id=models.IntegerField(primary_key=True)
    warehouse=models.ForeignKey(Warehouse,on_delete=models.CASCADE,blank=False,null=False)
    quantity=models.IntegerField()
    date= models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    def __str__(self):
        return str(self.order_id)
    @classmethod
    def search_by_id(cls,search_id):
        product=cls.objects.filter(order_id__icontains=search_id)
        return 



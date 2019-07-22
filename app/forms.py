from .models import *
from django import forms

'''
form to add new product to stock
'''
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude =['category']

'''
form to update the quantity of a product
'''

class UpdateProdQuantity(forms.ModelForm):
    class Meta:
        model = Order_Product
        fields =['quantity']

'''
form to add more items in a distributor that did 
not exist in their stock
'''

class NewHouseProd(forms.ModelForm):
    class Meta:
        model = House_Product
        exclude = ['warehouse','quantity']

'''
form to add  products in a specific distributor when running 
low on stock 
'''

class AddHouseProd(forms.ModelForm):
   class Meta:
       model = OrderDetails
       exclude = ['product','warehouse']


from .models import *
from django import forms

'''
form to add items to products in a specific location
'''

class NewProd(forms.ModelForm):
   class Meta:
       model = OrderDetails
       exclude = ['warehouse']

'''
form to add more items in a house when running
low on stock
'''

class NewHouseProd(forms.ModelForm):
    class Meta:
        model = House_Product
        exclude = ['warehouse','quantity']
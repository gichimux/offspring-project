from .models import *
from django import forms
import datetime

'''
New category
'''
class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        exclude =[]
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
        exclude = ['warehouse','quantity','category']

'''
form to add  products in a specific distributor when running 
low on stock 
'''

class AddHouseProd(forms.ModelForm):
    time = forms.DateTimeField(
        widget = forms.SelectDateWidget())
    class Meta:
        model = OrderDetails
        exclude = ['product','warehouse']

class DateForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)


'''
form for new supplier
'''
class NewSupplier(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = []

'''
New distributor
'''
class NewDistributor(forms.ModelForm):
    class Meta:
        model = Distributor
        exclude = []

'''
New customer
'''
class NewCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = []

class CustomerOrder(forms.ModelForm):
    time = forms.DateTimeField(
        widget = forms.SelectDateWidget())
    class Meta:
        model = Customer_order
        exclude = ['status','month','year',"sKU",'total_price']

class Invoicing(forms.ModelForm):
    class Meta:
        model = Invoice
        exclude = ['date']
 
class NewRequest(forms.ModelForm):
    time = forms.DateTimeField(
        widget = forms.SelectDateWidget())
    class Meta:
        
        model = Requested_supply
        exclude = ['supplier','status']
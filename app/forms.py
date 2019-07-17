from .models import *
from django import forms

class NewProd(forms.ModelForm):
   class Meta:
       model = OrderDetails
       exclude = ['warehouse']
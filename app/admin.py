from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Distributor)
admin.site.register(OrderDetails)
admin.site.register(House_Product)
admin.site.register(Supplier)
admin.site.register(Order_Product)
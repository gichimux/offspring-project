from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Distributor)
admin.site.register(OrderDetails)
admin.site.register(House_Product)
admin.site.register(Supplier)
admin.site.register(Order_Product)
admin.site.register(Customer_order)
admin.site.register(Customer)

admin.site.site_header = "Offspring";
admin.site.site_title = "Offspring Inventory ";
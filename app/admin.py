from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Distributor)
admin.site.register(OrderDetails)
admin.site.register(Sub_Category)

admin.site.site_header = "Offspring";
admin.site.site_title = "Offspring Inventory ";
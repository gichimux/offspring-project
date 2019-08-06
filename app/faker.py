from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
from .models import *
import random
import os

def fake_sales():

    warehouses=Distributor.objects.all()
    for warehouse in warehouses:
        h_products=warehouse.warehouse_products.all()
        
        for product in h_products:
            start_date=parser.parse("2019-01-01")
            end_date=parser.parse("2019-07-31")
            print(product)
            product.quantity= 1000
            product.save()
            orders=product.orders.all()
            orders.delete()
            if start_date<=end_date:
                while True:
                    start_date=start_date+relativedelta(months=1)
                    q=random.randint(20,100)
                    order=Customer_order(product=product,order_serial= os.urandom(4).hex(),time=start_date)
                    order.warehouse=product.warehouse
                    c=Customer(name=os.urandom(4).hex(),email=os.urandom(4).hex(),contact=os.urandom(4).hex())
                    c.save()
                    order.customer=c
                    order.quantity=q
                    order.save()
                    if start_date>=end_date:
                        break
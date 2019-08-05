from django.shortcuts import render
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAdminUser
IsAdminOrReadOnly=IsAdminUser
from django.core import serializers
import json
import datetime 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status

'''
View for pwa
'''
@login_required(login_url='/accounts/login/')
def base_layout(request):
	template='base.html'
	return render(request,template)

def test(request):
    return render(request, 'dashboard/index.html')

'''
View for the inventory page displaying categories
of items in stock
'''
@login_required(login_url='/accounts/login/')
def inventory(request):
    messages=None
    categories = Category.objects.all()
    if request.method == 'POST':
        form = NewCategory(request.POST, request.FILES)
        if form.is_valid():
            category=form.save(commit=False)
            category.save()
            return redirect(inventory)
    else:
        form =NewCategory()
    
    products = Product.objects.all()
    for product in products:
        if product.quantity < 80:
            message1 = 's are running low on stock'
            messages = product.name + ''+ message1
            print(messages)
           
        else:
            messages = None
    
    

    return render(request, 'stockmg/inventory.html', {'form':form,'messages':messages,'categories':categories})


'''
view for the single categories displaying
items under a category
'''
@login_required(login_url='/accounts/login/')
def stock_category(request,id):
    products = Product.objects.filter(category=id)
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.category=Category.objects.get(id=id)
            prod.save()
            return redirect(stock_category,id)
    else:
        form =AddProduct()
    return render(request,'stockmg/category.html',{'products':products,'category':category,'form':form})


'''
view for Single stock product under the respective
category
'''
@login_required(login_url='/accounts/login/')
def stock_product(request,id):
    to_add = Product.objects.get(id=id)
    
    if request.method == 'POST':
        form = UpdateProdQuantity(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.product=to_add
            to_add.quantity=product.quantity+to_add.quantity
            product.save()
            to_add.save()
            return redirect(stock_product,id)
    else:
        form =UpdateProdQuantity()

    return render(request,'stockmg/stock_product.html',{'to_add':to_add,'form':form})


'''
views for distributors
'''

'''
All distributors
'''
@login_required(login_url='/accounts/login/')
def all_distributors(request):
    houses = Distributor.objects.all()
    if request.method == 'POST':
        form = NewDistributor(request.POST, request.FILES)
        if form.is_valid():
            distributor=form.save(commit=False)
            distributor.save()
            return redirect(all_distributors)
    else:
        form =NewDistributor()
    return render(request,'distributor/distributors.html',{'houses':houses,'form':form})

'''
View for a single distributor displaying categories
'''
@login_required(login_url='/accounts/login/')
def single_house(request,id):
    categories = Category.objects.all()
    house = Distributor.objects.get(id=id)
    house_products = House_Product.objects.filter(warehouse=id)
    
    return render(request,'distributor/distributor.html',{'house':house,'categories':categories})


'''
view for the single categories within a distributor displaying
quantity of items under a category
'''
@login_required(login_url='/accounts/login/')
def house_category(request,h_id,c_id):
    message = None
    products = House_Product.objects.filter(category=c_id).filter(warehouse=h_id)
    category = Category.objects.get(id=c_id)
    house = Distributor.objects.get(id=h_id)
    if request.method == 'POST':
        form = NewHouseProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            try:
                no_repeat=House_Product.objects.filter(warehouse=house).get(name=item.name)
                
                message = 'That item already exists in this store'
            except ObjectDoesNotExist:
                item.warehouse=house
                item.category=category
                
                item.save()
                return redirect(house_category,h_id,c_id)
    else:
        form =NewHouseProd()
    
    return render(request,'distributor/categories.html',{'message':message,'products':products,'category':category,'house':house,'form':form})


'''
view for a single item within a distributor displaying single
products quantity within the distributor
'''

@login_required(login_url='/accounts/login/')
def add_house_product(request,h_id,i_id):
    message = None
    house = Distributor.objects.get(id=h_id)
    to_update = House_Product.objects.filter(warehouse=h_id).get(id=i_id) 
    product = Product.objects.get(name=to_update.name.name)
    if request.method == 'POST':
        form = AddHouseProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.product = product
            item.warehouse=house
            item.month=datetime.datetime.now().strftime ("%m")
            item.year=datetime.datetime.now().strftime ("%Y")
            prod=Product.objects.get(id=item.product.id)
            if prod.quantity < item.quantity:
                message = 'The amount of product in stock is not enough'
            else:
                prod.quantity = prod.quantity-item.quantity
                prod_add = House_Product.objects.filter(warehouse=h_id).get(name=prod)
                prod_add.quantity=prod_add.quantity+item.quantity
                item.save()
                prod_add.save()
                prod.save()
                message = None
                return redirect(add_house_product,h_id,i_id)
    else:
        form =AddHouseProd()
    
    return render(request,'distributor/item.html',{'message':message,'product':product,'house':house,'to_update':to_update,'form':form})

'''
view to search a particular product by its serial
'''
@login_required(login_url='/accounts/login/')
def search(request):
    if 'product' in request.GET and request.GET['product']:
        search_serial =request.GET.get("product")
        searched_product = House_Product.search_by_serial(search_serial)
        message=f"{search_serial}"
        return render(request,'search.html',{"message":message,"products":searched_order})
    else:
        message="You did not return any product"
        return render(request,'search.html',{"message":message})


'''
View for all the suppliers
'''
@login_required(login_url='/accounts/login/')
def all_suppliers(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = NewSupplier(request.POST, request.FILES)
        if form.is_valid():
            supplier=form.save(commit=False)
            supplier.save()
            return redirect(all_suppliers)
    else:
        form =NewSupplier()
    return render(request,'supplier/suppliers.html',{'suppliers':suppliers,'form':form})

'''
View for supplier details
'''
@login_required(login_url='/accounts/login/')
def single_supplier(request,id):
    supplier = Supplier.objects.get(id=id)
    orders = Order_Product.objects.filter(supplier=id)
    return render(request,'supplier/supplier.html',{'supplier':supplier,'orders':orders})


'''
View for all orders
'''
@login_required(login_url='/accounts/login/')
def all_orders(request):
    return render(request,'orders/orders.html')
'''
view for supply orders
'''
@login_required(login_url='/accounts/login/')
def supply_orders(request):
    orders = Order_Product.objects.order_by('-date').all()
    return render(request,'orders/supply_orders.html',{'orders':orders})

'''
View for all distributors transfers
'''
@login_required(login_url='/accounts/login/')
def transfer_orders(request):
    distributors = Distributor.objects.all()
    return render(request,'orders/transfer_orders.html',{'distributors':distributors})

'''
view for transfer orders by month
'''
@login_required(login_url='/accounts/login/')
def transfer_order_month(request,m):
    
    orders = OrderDetails.objects.filter(month=m)
    return render(request,'orders/transfers_by_month.html',{'orders':orders})

'''
view for single distributor orders
'''
@login_required(login_url='/accounts/login/')
def distributor_transfer_orders(request,id):
    orders = OrderDetails.objects.filter(warehouse=id).all()
    return render(request,'orders/distributor_transfers.html',{'orders':orders})

@login_required(login_url='/accounts/login/')
def distributor_sale(request):
    orders = Distributor_sale.objects.all()
    return render(request,'orders/distributor_sale.html',{'orders':orders})

'''
View for the distributor orders by the month
'''


'''
View for all distributors feedback on items sold
'''

@login_required(login_url='/accounts/login/')
def distributor_sale(request):
    orders = Distributor_sale.objects.all()
    return render(request,'orders/distributor_sale.html',{'distributors':distributors})

'''
View for a single distributors feedback on items sold
'''
@login_required(login_url='/accounts/login/')
def distributor_feedback(request,id):
    orders = Distributor_sell.objects.filter(warehouse=id).order_by('-date')
    return render(request,'orders/single_distri_feedback.html',{'orders':orders})


'''
Analysis view
'''

'''
All categories view 
'''
@login_required(login_url='/accounts/login/')
def full_stock(request):
    categories = Category.objects.all()
    

    return render(request, 'analysis/analysis.html', {'categories':categories})

'''
total items in stock  category analysis
'''
@login_required(login_url='/accounts/login/')
def full_category(request,id):
    products = Product.objects.filter(category=id)
    category = Category.objects.get(id=id)
    return render(request,'analysis/category_analysis.html',{'products':products,'category':category})


def aggregateOrdersBymonth(orders):
    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    orders_={i:[] for i in months}
    for i in orders:
        orders_[months[i["time"].date().month -1]].append(i["quantity"])
    for k,v in orders_.items():
        orders_[k]=sum(v)
    return orders_



'''
single item stock analysis 
'''
@login_required(login_url='/accounts/login/')
def product_analysis(request,id):
    to_add = Product.objects.get(id=id)
    orders=[]
    for w in to_add.location.all():
        orders=[{"quantity":i.quantity,"time":i.time} for i in w.orders.all()]
    data=json.dumps(aggregateOrdersBymonth(orders))
    print(type(data))

    products = House_Product.objects.filter(name=id) 
    in_houses = House_Product.objects.filter(name=id) \
    .values('warehouse') \
    .values('quantity') \
    
    print(in_houses)

    return render(request,'analysis/stock_product_analysis.html',{'to_add':to_add,'in_houses':in_houses,'products':products,"data":data})

'''
all cusomers
'''

@login_required(login_url='/accounts/login/')
def all_customers(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = NewCustomer(request.POST, request.FILES)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.save()
            return redirect(all_customers)
    else:
        form =NewCustomer()
    return render(request,'customer/customers.html',{'customers':customers,'form':form})

'''
Customer order processing
'''

@login_required(login_url='/accounts/login/')
def customer_order(request):
    message1=None
    message2=None
    message3=None
    orders = Customer_order.objects.order_by('-date').all()
    if request.method == 'POST':
        form = CustomerOrder(request.POST, request.FILES)
        if form.is_valid():
            date_str=form.cleaned_data["date"]
            # from dateutil import parser
            # date_=parser.parse(date_str)
          
            order=form.save(commit=False)
            order.time=date_str
            # order.month = datetime.datetime.now().strftime ("%m")
            # order.year = datetime.datetime.now().strftime ("%y")
            try:
                
                # product = Product.objects.get(sKU=order.sKU)
                order.sKU=order.product.name.sKU
                product=order.product.name
                order.total_price = order.quantity * product.unit_price
            except ObjectDoesNotExist as e:
                print(e)
                message3='Make sure you input the SKU correctly'

            try:
                to_subtract = House_Product.objects.filter(warehouse=order.warehouse).get(sKU=order.sKU)
                if order.quantity > to_subtract.quantity:
                    message2 = 'The amount of product in this warehouse is not enough'
                else:
                    to_subtract.quantity=to_subtract.quantity - order.quantity
                    to_subtract.save()
                    print("i reached here")
                    order.save()
                    return redirect(customer_order)
            except ObjectDoesNotExist as e:
                print(e)
                message1='The prduct does not exist in that warehouse'
        else:
            print(form.errors)
            
    else:
       
        form =CustomerOrder()
    
    return render(request,'customer/customers_order.html',{'orders':orders,'form':form,'message1':message1,'message2':message2,'message3':message3})

'''
generating invoice
'''
@login_required(login_url='/accounts/login/')
def generate_invoice(request):
    invoices=Invoice.objects.order_by('-date').all()
    if request.method == 'POST':
        form = Invoicing(request.POST, request.FILES)
        if form.is_valid():
            invoice=form.save(commit=False)
            invoice.save()
            return redirect('customers_invoice',invoice.order.order_serial,invoice.id)
    else:
        form = Invoicing()

    return render(request,'customer/generate_invoice.html',{'form':form,'invoices':invoices})
'''
Invoice
'''
@login_required(login_url='/accounts/login/')
def customers_invoice(request,serial,id):
    invoice = Invoice.objects.get(id=id)
    orders = Customer_order.objects.filter(order_serial=serial)
    orders_c = Customer_order.objects.filter(order_serial=serial)
    lst=[]
    for order in orders_c:
        lst.append(order.total_price)
        total=sum(lst)
    
    return render(request,'customer/invoice.html',{'orders':orders,'total':total,'invoice':invoice})
    


'''
Api views
'''
class CategoriesList(APIView):
    def get(self, request, format=None):
        all_projects = Category.objects.all()
        serializers = CategorySerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class DistributorsList(APIView):
    def get(self, request, format=None):
        all_projects = Distributor.objects.all()
        serializers = DistributorSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = DistributorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class SuppliersList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Supplier.objects.all()
        serializers = SupplierSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SupplierSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def customerApiViews(request):
    # orders=Customer_order.objects.all()
    # x=[]
    # for i in orders:
    #     x.append({"quantity":i.quantity,"time":i.time,"product":i.product.name.name})

    x={}
    products=Product.objects.all()
    for p in products:
        x[p.sKU]=[]
        for w in p.location.all():
            x[p.sKU]=[{"quantity":i.quantity,"time":i.time,"product":i.product.name.name} for i in w.orders.all()]
    from django.http import JsonResponse
    return JsonResponse({"data":x})
        
# def xss(request):
#     import csv
#     from django.http import JsonResponse
#     from django.conf import settings
#     path=settings.BASE_DIR+"/app/data/combined.csv"
#     with open(path,"r") as infile:
#         data=csv.DictReader(infile)
#         x=[dict(i) for i in data]
#     return JsonResponse({"data":x})
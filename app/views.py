from django.shortcuts import render
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist

'''
View for the inventory page displaying categories
of items in stock
'''
def inventory(request):
    houses = Distributor.objects.all()
    products = Product.objects.all()
    for product in products:
        if product.quantity < 80:
            message1 = 's are running low on stock'
            messages = product.name + ''+ message1
            print(messages)
           
        else:
            messages = ''
    categories = Category.objects.all()
    

    return render(request, 'inventory.html', {'messages':messages,'product':product,'houses':houses,'categories':categories})


'''
view for the single categories displaying
items under a category
'''

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
    return render(request,'category.html',{'products':products,'category':category,'form':form})

'''
view for Single stock product under the respective
category
'''

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

    return render(request,'stock_product.html',{'to_add':to_add,'form':form})


'''
views for distributors
'''

'''
View for a single distributor displaying categories
'''

def single_house(request,id):
    categories = Category.objects.all()
    house = Distributor.objects.get(id=id)
    house_products = House_Product.objects.filter(warehouse=id)
    
    return render(request,'distributor/house.html',{'house':house,'categories':categories})


'''
view for the single categories within a distributor displaying
quantity of items under a category
'''

def house_category(request,h_id,c_id):
    message = ''
    products = House_Product.objects.filter(warehouse=h_id).filter(category=c_id)
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
                return redirect(inventory)
    else:
        form =NewHouseProd()
    
    return render(request,'distributor/h_category.html',{'message':message,'products':products,'category':category,'house':house,'form':form})


'''
view for a single item within a distributor displaying single
products quantity within the distributor
'''


def add_house_product(request,h_id,i_id):
    message = ''
    house = Distributor.objects.get(id=h_id)
    product = Product.objects.get(id=i_id)
    to_update = House_Product.objects.filter(warehouse=h_id).get(name=product) 
    if request.method == 'POST':
        form = AddHouseProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.product = product
            item.warehouse=house
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
                message = ''
                return redirect(add_house_product,h_id,i_id)
    else:
        form =AddHouseProd()
    return render(request,'distributor/item.html',{'message':message,'product':product,'house':house,'to_update':to_update,'form':form})

'''
view to search a particular product by its serial
'''

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
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request,'supplier/suppiers.html',{'suppiers':suppliers})

'''
View for supplier details
'''
def single_supplier(request,id):
    supplier = Supplier.objects.get(id=id)

    return render(request,'supplier/supplier.html',{'supplier':supplier})


'''
Analysis view
'''

'''
All categories view 
'''

def full_stock(request):
    categories = Category.objects.all()
    

    return render(request, 'analysis/analysis.html', {'categories':categories})

'''
total items in stock  category analysis
'''
def full_category(request,id):
    products = Product.objects.filter(category=id)
    category = Category.objects.get(id=id)
    return render(request,'analysis/category_analysis.html',{'products':products,'category':category})


'''
single item stock analysis 
'''

def product_analysis(request,id):
    to_add = Product.objects.get(id=id)
    products = House_Product.objects.filter(name=id) 
    in_houses = House_Product.objects.filter(name=id) \
    .values('warehouse') \
    .values('quantity') \
    
    print(in_houses)

    return render(request,'analysis/stock_product_analysis.html',{'to_add':to_add,'in_houses':in_houses,'products':products})

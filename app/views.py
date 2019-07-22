from django.shortcuts import render
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

'''
View for the inventory page displaying categories
of items in stock
'''
def inventory(request):
    houses = Distributor.objects.all()
    objects = Product.objects.all()
    categories = Category.objects.all()
    

    return render(request, 'inventory.html', {'objects':objects,'houses':houses,'categories':categories})


'''
view for the single categories
'''

def category(request,id):
    products = Product.objects.filter(category=id)
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.category=Category.objects.get(id=id)
            prod.save()
            return redirect(inventory)
    else:
        form =AddProduct()
    return render(request,'category.html',{'products':products,'category':category,'form':form})

'''
view for Single stock product
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
            return redirect(inventory)
    else:
        form =UpdateProdQuantity()

    return render(request,'stock_product.html',{'to_add':to_add,'form':form})

'''
View for a single distributor
'''

def single_house(request,id):

    house = Distributor.objects.get(id=id)
    house_products = House_Product.objects.filter(warehouse=id)
    if request.method == 'POST':
        form = NewHouseProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.warehouse=house
            item.save()
            return redirect(news_today)
    else:
        form =NewHouseProd()
    return render(request,'distributor/house.html',{'house':house,'form':form,'products':house_products})


'''
view for a single item within a distributor 
'''


def add_house_product(request,h_id,i_id):
    house = Distributor.objects.get(id=h_id)
    product = Product.objects.get(id=i_id)
    to_update = House_Product.objects.get(name=product) 
    if request.method == 'POST':
        form = AddHouseProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.product = product
            item.warehouse=house
            prod=Product.objects.get(id=item.product.id)
            prod.quantity = prod.quantity-item.quantity
            prod_add = House_Product.objects.get(name=prod)
            prod_add.quantity=prod_add.quantity+item.quantity
            item.save()
            prod_add.save()
            prod.save()
            return redirect(news_today)
    else:
        form =AddHouseProd()
    return render(request,'distributor/item.html',{'product':product,'house':house,'to_update':to_update,'form':form})

def search(request):
    if 'product' in request.GET and request.GET["product"]:
        search_serial =request.GET.get("product")
        searched_products = House_Product.search_by_serial(search_serial)
        message=f"{search_serial}"
        return render(request,'search.html',{"message":message,"products":searched_products})
    else:
        message="You did not search using a serial"

    return render(request,'search.html',{"message":message})

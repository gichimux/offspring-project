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


   return render(request, 'vendors.html', {'objects':objects,'houses':houses})

'''
View for a single distributor
'''
def single_house(request,id):

   house = House.objects.get(id=id)
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
    return render(request,'house.html',{'house':house,'form':form,'products':house_products})
'''
view for a single item within a distributor 
'''


def add_item(request,h_id,i_id):
    house = House.objects.get(id=h_id)
    product = MoringaMerch.objects.get(id=i_id)
    to_update = House_Product.objects.get(name=product) 
    if request.method == 'POST':
        form = NewProd(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.product = product
            item.warehouse=house
            prod=MoringaMerch.objects.get(id=item.product.id)
            prod.quantity = prod.quantity-item.quantity
            prod_add = House_Product.objects.get(name=prod)
            prod_add.quantity=prod_add.quantity+item.quantity
            item.save()
            prod_add.save()
            prod.save()
            return redirect(news_today)
    else:
        form =NewProd()
    return render(request,'item.html',{'product':product,'house':house,'to_update':to_update,'form':form})



def search(request):
    if 'product' in request.GET and request.GET['product']:
        search_id =request.GET.get("product")
        searched_order = OrderDetails.search_by_id(search_id)
        message=f"{search_id}"
        return render(request,'index.html',{"message":message,"products":searched_order})
    else:
        message="You did not return any product"
        return render(request,'index.html',{"message":message})

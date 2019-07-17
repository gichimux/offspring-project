from django.shortcuts import render
from .models import *
from .forms import *


def news_today(request):
   houses = Warehouse.objects.all()
   objects = Product.objects.all()


   return render(request, 'vendors.html', {'objects':objects,'houses':houses})
def house(request,id):

   house = Warehouse.objects.get(id=id)
   house_orders=OrderDetails.objects.filter(warehouse=id)

   if request.method == 'POST':
       form = NewProd(request.POST, request.FILES)
       if form.is_valid():
           item = form.save(commit=False)
           item.warehouse=house
           prod=Product.objects.get(id=item.product.id)
           prod.quantity = prod.quantity-item.quantity
           print(prod.quantity)
           prod.save()
           item.save()
           return redirect(news_today)
   else:
       form =NewProd()
   return render(request,'house.html',{'house':house,'form':form,'orders':house_orders})

def search(request):
    if 'product' in request.GET and request.GET['product']:
        search_id =request.GET.get("product")
        searched_order = OrderDetails.search_by_id(search_id)
        message=f"{search_id}"
        return render(request,'index.html',{"message":message,"products":searched_order})
    else:
        message="You did not return any product"
        return render(request,'index.html',{"message":message})
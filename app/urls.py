from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$',views.inventory,name='inventory'),
 url(r'^search/',views.search,name='search_results'),
 url(r'^category/(\d+)$',views.stock_category,name='category'),
 url(r'^category/product/(\d+)$',views.stock_product,name="stock_product"),

 url(r'^house/(\d+)$',views.single_house,name="single_house"),
 url(r'^house/category/(\d+)/(\d+)$',views.house_category,name="house_category"),
 url(r'^house/category/product/(\d+)/(\d+)$',views.add_house_product,name="add_house_product"),

 url(r'^supplier$',views.suppliers,name="suppliers"),
 url(r'^supplier/(\d+)$',views.single_supplier,name="single_supplier"),
     
 url(r'^analysis$',views.full_stock,name='analysis'),
 url(r'^analysis/category/(\d+)$',views.full_category,name='category_analysis'),
 url(r'^analysis/category/product/(\d+)$',views.product_analysis,name="stock_product_analysis"),  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
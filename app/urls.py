from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$',views.inventory,name='inventory'),
 url(r'^search/',views.search,name='search_results'),
 url(r'^category/(\d+)$',views.stock_category,name='category'),
 url(r'^category/product/(\d+)$',views.stock_product,name="stock_product"),
     
 url(r'^houses$',views.all_distributors,name='distributors'),
 url(r'^house/(\d+)$',views.single_house,name="single_house"),
 url(r'^house/category/(\d+)/(\d+)$',views.house_category,name="house_category"),
 url(r'^house/category/product/(\d+)/(\d+)$',views.add_house_product,name="add_house_product"),

 url(r'^supplier$',views.all_suppliers,name="suppliers"),
 url(r'^supplier/(\d+)$',views.single_supplier,name="supplier"),
 url(r'^status/(\d+)$',views.product_status,name='status'),

 url(r'^orders$',views.all_orders,name="orders"),
 url(r'^orders/supplier$',views.supply_orders,name='supply_orders'),
 url(r'^orders/distributors$',views.transfer_orders,name='transfer_orders'),
 url(r'^orders/distributors/(\d+)$',views.distributor_transfer_orders,name="dis_transfer_ord"),
 url(r'^orders/month/',views.transfer_order_month,name="month"),

 url(r'^analysis$',views.full_stock,name='analysis'),
 url(r'^analysis/category/(\d+)$',views.full_category,name='category_analysis'),
 url(r'^analysis/category/product/(\d+)$',views.product_analysis,name="stock_product_analysis"), 

 url(r'^customer$',views.all_customers,name="customers"),
 url(r'^customer/order$',views.customer_order,name="customer_orders"),
 url(r'^invoice/(\w+)/(\d+)$',views.customers_invoice,name="customers_invoice"),
 url(r'^new/invoice$',views.generate_invoice,name="generate_invoice"),


 url(r'^distributors',views.DistributorsList.as_view()),
 url(r'^suppliers',views.SuppliersList.as_view()),
 url(r'^categories',views.CategoriesList.as_view()),
 
 url(r'^report',views.generate_report,name="month_report"),
url(r'^customer-orders',views.customerApiViews,name="customers-orders")


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$',views.inventory,name='inventory'),
 url(r'^search/',views.search,name='search_results'),
 url(r'^category/(\d+)$',views.category,name='category'),
 url(r'^house/(\d+)$',views.single_house,name="house"),
 url(r'^house/update(\d+)/(\d+)$',views.add_house_product,name="add_product"),
 url(r'^category/product/(\d+)$',views.stock_product,name="stock_product"),  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
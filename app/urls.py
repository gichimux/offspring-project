from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.inventory,name='home'),
    url(r'^search/',views.search,name='search_results'),
    url(r'add/(\d+)/(\d+)',views.add_item,name="add"),
    url(r'house/(\d+)',views.single_house,name="house"), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

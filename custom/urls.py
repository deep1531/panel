from django.contrib import admin
from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('',dashboard,name='dashboard'),
    path('home/',home,name='home'),
    path('order/',order,name='order'),
    path('product',product,name='product'),
    path('delete/<id>/', delete, name = "delete"),
    path('update/<id>/', update, name = "update"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
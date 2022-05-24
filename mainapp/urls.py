from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('ice', ice, name='ice'),
    path('delivery', delivery, name='delivery'),
    path('zebartools', zebartools, name='zebartools'),
    path('contacts', contacts, name='contacts'),
    path('ice_type/<int:ice_id>/', view_ice_type, name='view_ice_type'),
    path('zebartools/<int:product_id>/', view_zebartools_product, name='view_zebartools_product'),
]

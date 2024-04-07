from django.contrib import admin
from django.urls import path, include
from .views import main_page, about, fake_client, fake_product, \
 fake_order, show_order, upload_image


urlpatterns = [
 path('', main_page, name='main'),
 path('about/', about, name='about'),
 path('fc/', fake_client, name='fake_client'),
 path('fp/', fake_product, name='fake_product'),
 path('fo/', fake_order, name='fake_order'),
 path('show/<int:period>', show_order, name='show_order'),
 path('prod_form', upload_image, name='upload_image'),


]

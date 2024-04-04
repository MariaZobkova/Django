from django.contrib import admin
from django.urls import path, include
from .views import main_page, about, fake_client, fake_product


urlpatterns = [
 path('', main_page, name='main'),
 path('about/', about, name='about'),
 path('fc/', fake_client, name='fake_client'),
 path('fp/', fake_product, name='fake_product'),


]

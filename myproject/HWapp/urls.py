from django.contrib import admin
from django.urls import path, include
from .views import main_page, about


urlpatterns = [
 path('', main_page, name='main'),
 path('about/', about, name='about'),

]

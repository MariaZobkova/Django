from django.contrib import admin
from django.urls import path, include
from .views import index, eagle_tails, game_dice, game_numbers, coin_values


urlpatterns = [
 path('', index, name='index'),
 path('eagle/', eagle_tails, name='eagle'),
 path('game/', game_dice, name='game'),
 path('numbers/', game_numbers, name='numbers'),
 path('eagle_val/', coin_values, name='eagle_val'),




]

from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Coin


def index(request):
 return HttpResponse("Hello, world!")


def eagle_tails(request):
 result = choice(["Орел", "Решка"])
 side = Coin(side=result)
 side.save()
 return HttpResponse(str(result))


def game_dice(request):
 return HttpResponse(str(randint(1, 7)))


def game_numbers(request):
 return HttpResponse(str(randint(0, 101)))


def coin_values(request):
 value = Coin.last_values()
 lst = []
 for i in value:
  lst.append(i.side)
 return HttpResponse(lst)






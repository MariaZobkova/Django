from django.shortcuts import render
from django.http import HttpResponse
from random import *


def index(request):
 return HttpResponse("Hello, world!")


def eagle_tails(request):
 return HttpResponse(choice(["Орел", "Решка"]))


def game_dice(request):
 return HttpResponse(str(randint(1, 7)))


def game_numbers(request):
 return HttpResponse(str(randint(0, 101)))






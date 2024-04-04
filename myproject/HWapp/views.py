from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product


def main_page(request):
    main_html = "<h1>Сайт о помидорах</h1><p>Тут присутвует вся информация о помидорах! Нужно только поискать</p>"
    return HttpResponse(main_html)

def about(request):
    about_html = "<h1>О себе</h1><p>Данный сайт создает большой любитель помидор, мечтающий стать разработчиком</p>"
    return HttpResponse(about_html)

def fake_client(request):
    for i in range(11):
        client = Client(name=f'name{i}')
        client.save()
    return HttpResponse("Добавлено 10 клиентов")

def fake_product(request):
    for i in range(11):
        product = Product(name=f'product{i}', price=856.85)
        product.save()
    return HttpResponse("Добавлено 10 товаров")


from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    main_html = "<h1>Сайт о помидорах</h1><p>Тут присутвует вся информация о помидорах! Нужно только поискать</p>"
    return HttpResponse(main_html)

def about(request):
    about_html = "<h1>О себе</h1><p>Данный сайт создает большой любитель помидор, мечтающий стать разработчиком</p>"
    return HttpResponse(about_html)
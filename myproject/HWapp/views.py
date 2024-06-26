import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from .forms import ProductForm

from .models import Client, Product, Order


def main_page(request):
    return render(request, 'HWapp/base.html')


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


def fake_order(request):
    client = Client.objects.filter(name="name1").first()
    product1 = Product.objects.get(id="1")
    product2 = Product.objects.get(id="2")
    for i in range(1):
        order = Order(customer=client, total_price=product1.price + product2.price, date_ordered='2023-01-01')
        order.save()
        order.products.add(product1)
        order.products.add(product2)
        order.save()

    return HttpResponse("Добавлен 1 заказ")


def show_order(request, period):
    global title
    current_datetime = datetime.date.today()
    client = Client.objects.get(id='1')
    if period == 30:
        title = "За Месяц"
        orders = Order.objects.filter(customer=client, date_ordered__month=current_datetime.month)
    elif period == 365:
        title = "За год"
        orders = Order.objects.filter(customer=client, date_ordered__year=current_datetime.year)
    elif period == 7:
        title = "За неделю"
        orders = Order.objects.filter(customer=client, date_ordered=current_datetime)
    product_list = []
    for order in orders:
        if order.products:
            product_list.append(order.products.all())

    context = {"title": title, "orders": product_list}
    return render(request, 'HWapp/catalog_orders.html', context)


def upload_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
            product = Product(name=name, description=description, price=price,
                               count=count, image=image)

            product.save()
    else:
        form = ProductForm()
    return render(request, 'HWapp/upload_image.html', {'form':
                                                        form})


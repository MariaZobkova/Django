from datetime import datetime

from django.db import models
# —оздайте три модели Django: клиент, товар и заказ.
#
#  лиент может иметь несколько заказов. «аказ может содержать несколько товаров. “овар может входить в несколько заказов.
#
# ѕол€ модели Ђ лиентї:
# Ч им€ клиента
# Ч электронна€ почта клиента
# Ч номер телефона клиента
# Ч адрес клиента
# Ч дата регистрации клиента
#
# ѕол€ модели Ђ“оварї:
# Ч название товара
# Ч описание товара
# Ч цена товара
# Ч количество товара
# Ч дата добавлени€ товара
#
# ѕол€ модели Ђ«аказї:
# Ч св€зь с моделью Ђ лиентї, указывает на клиента, сделавшего заказ
# Ч св€зь с моделью Ђ“оварї, указывает на товары, вход€щие в заказ
# Ч обща€ сумма заказа
# Ч дата оформлени€ заказа
#
# ƒопишите несколько функций CRUD дл€ работы с модел€ми по желанию. „то по вашему мнению актуально в такой ба

class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'name: {self.name}, phone: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True)


    def __str__(self):
        return f'name: {self.name}, price: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(default=datetime.now)
    # auto_now_add = True
    def __str__(self):
        return f'customer: {self.customer}, products: {self.products}, "total_price": {self.total_price},' \
               f'"date_ordered": {self.date_ordered}'



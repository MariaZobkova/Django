from datetime import datetime

from django.db import models
# �������� ��� ������ Django: ������, ����� � �����.
#
# ������ ����� ����� ��������� �������. ����� ����� ��������� ��������� �������. ����� ����� ������� � ��������� �������.
#
# ���� ������ �������:
# � ��� �������
# � ����������� ����� �������
# � ����� �������� �������
# � ����� �������
# � ���� ����������� �������
#
# ���� ������ ������:
# � �������� ������
# � �������� ������
# � ���� ������
# � ���������� ������
# � ���� ���������� ������
#
# ���� ������ ������:
# � ����� � ������� �������, ��������� �� �������, ���������� �����
# � ����� � ������� ������, ��������� �� ������, �������� � �����
# � ����� ����� ������
# � ���� ���������� ������
#
# �������� ��������� ������� CRUD ��� ������ � �������� �� �������. ��� �� ������ ������ ��������� � ����� ��

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



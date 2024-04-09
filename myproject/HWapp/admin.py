from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    ordering = ['price', '-count']
    list_filter = ['price']


admin.site.register(Product, ProductAdmin)





from django import forms
from .models import *

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(required=False)
    price = forms.FloatField()
    count = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)




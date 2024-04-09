from django.db import models
from django.utils import timezone

# Create your models here.

class Coin(models.Model):
    time = models.DateTimeField(default=timezone.now())
    side = models.CharField(max_length=10)

    @staticmethod
    def last_values():
        value = Coin.objects.order_by('-time')[:5]
        return value

    def __str__(self):
        return f'{self.side}, {self.time}'


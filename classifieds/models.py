from django.db import models

from utils.fields import CurrencyField


class Price(models.Model):
    currency = CurrencyField()
    amount = models.DecimalField(max_digits=10, decimal_places=5)


class Classified(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField()
    price = models.OneToOneField(Price, null=True, blank=True, on_delete=models.SET_NULL, related_name='classified')
    created = models.DateTimeField(auto_now_add=True)

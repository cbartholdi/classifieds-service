from django.db import models

from utils.fields import CurrencyField


class Classified(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField()


class ClassifiedPrice(models.Model):
    classified = models.ForeignKey(Classified, on_delete=models.CASCADE)
    currency = CurrencyField()
    amount = models.DecimalField(max_digits=10, decimal_places=5)

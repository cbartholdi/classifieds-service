from django.db import models


CURRENCIES = (
    ('SEK', 'SEK'),
    ('EUR', 'EUR'),
)


class CurrencyField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = kwargs.get('choices', CURRENCIES)
        kwargs['default'] = kwargs.get('default', CURRENCIES[0])
        kwargs['max_length'] = kwargs.get('max_length', 3)
        kwargs['blank'] = kwargs.get('blank', False)
        super(CurrencyField, self).__init__(*args, **kwargs)

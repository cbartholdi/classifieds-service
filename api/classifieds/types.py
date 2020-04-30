from graphene_django.types import DjangoObjectType
from graphene import Field

from classifieds.models import Classified, Price


class PriceType(DjangoObjectType):
    class Meta:
        model = Price


class ClassifiedType(DjangoObjectType):
    price = Field(PriceType)

    class Meta:
        model = Classified



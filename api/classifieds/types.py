from graphene_django.types import DjangoObjectType

from classifieds.models import Classified, ClassifiedPrice


class ClassifiedType(DjangoObjectType):
    class Meta:
        model = Classified


class PriceType(DjangoObjectType):
    class Meta:
        model = ClassifiedPrice
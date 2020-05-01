import graphene
from graphene import String
from graphql import GraphQLError

from api.classifieds.constants import SORT_PRICE, SORT_CREATED, ORDERING_MAPPER, DESC_SIGNAL, Responses
from api.classifieds.types import ClassifiedType
from classifieds.models import Classified


class ClassifiedsQuery(object):
    all_classifieds = graphene.List(ClassifiedType,
                                    order_by=String(default_value=SORT_PRICE),
                                    ordering=String(default_value=DESC_SIGNAL))

    def resolve_all_classifieds(self, info, order_by, ordering):
        try:
            if order_by not in (SORT_PRICE, SORT_CREATED):
                raise ValueError
            if ordering not in ORDERING_MAPPER:
                raise ValueError

            order = f'{ORDERING_MAPPER.get(ordering)}{order_by}'

            return Classified.objects.order_by(order).select_related('price')

        except ValueError:
            raise GraphQLError(Responses.ILLEGAL_ARGUMENT.value)
        except Exception:
            raise GraphQLError(Responses.INTERNAL_ERROR.value)

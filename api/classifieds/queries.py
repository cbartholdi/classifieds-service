import graphene
from graphql import GraphQLError

from api.classifieds.constants import SORT_PRICE, SORT_CREATED, ORDERING_MAPPER
from api.classifieds.types import ClassifiedType
from classifieds.models import Classified


class ClassifiedsQuery(object):
    all_classifieds = graphene.List(ClassifiedType)

    def resolve_all_classifieds(self, info, order_by='created', ordering='desc'):

        """
        A way of fetching existing ads. It should be possible to sort the ads on the time they
        were inserted and by their price
        """

        # Order by both price and created combined? use sorted lambda...

        try:
            if order_by not in (SORT_PRICE, SORT_CREATED):
                raise Exception  # <- custom exception!
            if ordering not in ORDERING_MAPPER:
                raise Exception  # <- custom exception!

            order_by = f'{ORDERING_MAPPER.get(ordering)}{order_by}'

            return Classified.objects.order_by(order_by).select_related('price')
        except Exception:
            raise GraphQLError('OR JUST ERROR CODE LIKE IN MUTATION?')



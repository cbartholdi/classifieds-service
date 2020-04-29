import graphene

from api.classifieds.types import ClassifiedType
from classifieds.models import Classified


class ClassifiedsQuery(object):
    all_classifieds = graphene.List(ClassifiedType)

    def resolve_all_classifieds(self, info, **kwargs):
        return Classified.objects.all()

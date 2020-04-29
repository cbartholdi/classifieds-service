import graphene

from api.classifieds.queries import ClassifiedsQuery
from api.classifieds.mutations import CreateClassifiedMutation


class Query(graphene.ObjectType, ClassifiedsQuery):
    pass


class Mutation(graphene.ObjectType):
    create_classified = CreateClassifiedMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
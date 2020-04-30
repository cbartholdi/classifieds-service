import graphene

from api.classifieds.queries import ClassifiedsQuery
from api.classifieds.mutations import CreateClassifiedMutation, DeleteClassifiedMutation


class Query(graphene.ObjectType, ClassifiedsQuery):
    pass


class Mutation(graphene.ObjectType):
    create_classified = CreateClassifiedMutation.Field()
    delete_classified = DeleteClassifiedMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
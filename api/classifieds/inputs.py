from graphene import Float, InputObjectType, String


class PriceInput(InputObjectType):
    currency = String(required=True)
    amount = Float(required=True)

import graphene
from graphene import String, Field, Boolean, Argument, ID

from api.classifieds.inputs import PriceInput
from api.classifieds.types import ClassifiedType, PriceType
from classifieds.models import Classified, ClassifiedPrice


class CreateClassifiedMutation(graphene.Mutation):

    class Arguments:
        subject = String(required=True)
        body = String(required=True)
        email = String(required=True)
        price = Argument(PriceInput)

    ok = Boolean()
    error_code = String()
    classified = Field(ClassifiedType)
    price = Field(PriceType)

    def mutate(self, info, subject, body, email, price=None):
        ok = False
        classified, classified_price, error_code = None, None, None

        try:
            classified = Classified.objects.create(
                subject=subject,
                body=body,
                email=email
            )

            if price:
                classified_price = ClassifiedPrice.objects.create(
                    classified=classified,
                    amount=price.amount,
                    currency=price.currency
                )

            ok = True

        except Exception:
            error_code = 500

        return CreateClassifiedMutation(ok=ok, error_code=error_code, classified=classified, price=classified_price)


class DeleteClassifiedMutation(graphene.Mutation):

    class Arguments:
        classified_id = ID(required=True)

    ok = Boolean()
    error_code = String()

    def mutate(self, info, classified_id):
        ok = False
        error_code = None

        try:
            Classified.objects.get(id=classified_id).delete()
            ok = True
        except Exception:
            error_code = 500

        return DeleteClassifiedMutation(ok=ok, error_code=error_code)

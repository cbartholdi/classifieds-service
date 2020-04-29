import graphene
from graphene import String, Field, Boolean, Argument

from api.classifieds.inputs import PriceInput
from api.classifieds.types import ClassifiedType
from classifieds.models import Classified, ClassifiedPrice


class CreateClassifiedMutation(graphene.Mutation):

    class Arguments:
        subject = String(required=True)  # is True/False default? Unnecessary to set otherwise!
        body = String(required=True)
        email = String(required=True)
        price = Argument(PriceInput, required=False)

    ok = Boolean()
    error_code = String()
    classified = Field(ClassifiedType)

    def mutate(self, info, subject, body, email, price=None):
        ok = False
        classified, error_code = None, None

        try:
            classified = Classified.objects.create(
                subject=subject,
                body=body,
                email=email
            )

            if price:
                ClassifiedPrice.objects.create(
                    classified=classified,
                    amount=price.amount,
                    currency=price.currency
                )

            ok = True

        except Exception: # Custom exceptions!
            error_code = 500

        return CreateClassifiedMutation(ok=ok, error_code=error_code, classified=classified)

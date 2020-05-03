import graphene
from django.core.exceptions import ValidationError
from django.db import transaction
from graphene import String, Field, Boolean, Argument, ID

from api.classifieds.constants import Responses
from api.classifieds.inputs import PriceInput
from api.classifieds.types import ClassifiedType
from classifieds.models import Classified, Price


class CreateClassifiedMutation(graphene.Mutation):

    class Arguments:
        subject = String(required=True)
        body = String(required=True)
        email = String(required=True)
        price = Argument(PriceInput)

    ok = Boolean()
    error_code = String()
    classified = Field(ClassifiedType)

    def mutate(self, info, subject, body, email, price=None):
        ok = False
        classified, error_code = None, None

        try:
            kwargs = dict(subject=subject, body=body, email=email)

            Price(**price).full_clean() if price else None
            Classified(**kwargs).full_clean()

            kwargs.update(price=Price.objects.create(**price) if price else None)

            classified = Classified.objects.create(**kwargs)

            ok = True

        except ValidationError:
            error_code = Responses.ILLEGAL_ARGUMENT.value
        except Exception:
            error_code = Responses.INTERNAL_ERROR.value

        return CreateClassifiedMutation(ok=ok, error_code=error_code, classified=classified)


class DeleteClassifiedMutation(graphene.Mutation):

    class Arguments:
        classified_id = ID(required=True)

    ok = Boolean()
    error_code = String()

    def mutate(self, info, classified_id):
        ok = False
        error_code = None

        try:
            with transaction.atomic():
                Price.objects.filter(classified=classified_id).delete()
                Classified.objects.get(id=classified_id).delete()

                ok = True

        except (Classified.DoesNotExist, Price.DoesNotExist):
            error_code = Responses.NOT_FOUND.value

        except Exception:
            error_code = Responses.INTERNAL_ERROR.value

        return DeleteClassifiedMutation(ok=ok, error_code=error_code)

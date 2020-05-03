from enum import Enum


SORT_PRICE = 'price'
SORT_CREATED = 'created'

ASC_SIGNAL = 'asc'
DESC_SIGNAL = 'desc'


ORDERING_MAPPER = {
    ASC_SIGNAL: '',
    DESC_SIGNAL: '-',
}

SORT_MAPPER = {
    SORT_PRICE: 'price__amount',
    SORT_CREATED: SORT_CREATED
}


class Responses(Enum):
    NOT_FOUND = 'NotFound'
    INTERNAL_ERROR = 'InternalError'
    ILLEGAL_ARGUMENT = 'IllegalArgument'

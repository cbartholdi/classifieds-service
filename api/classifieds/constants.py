from enum import Enum


SORT_PRICE = 'price'
SORT_CREATED = 'created'

ASC_SIGNAL = 'asc'
DESC_SIGNAL = 'desc'


ORDERING_MAPPER = {
    ASC_SIGNAL: '',
    DESC_SIGNAL: '-',
}


class Responses(Enum):
    NOT_FOUND = 'NotFound'
    INTERNAL_ERROR = 'InternalError'
    ILLEGAL_ARGUMENT = 'IllegalArgument'

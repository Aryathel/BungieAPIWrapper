from datetime import datetime
from typing import (
    Optional,
    Union
)

from . import errors


__all__ = [
    'ValidatedDatetime',

    'parse_datetime',
    'process_errors',
]


DATETIME_FMTS = [
    '%Y-%m-%dT%H:%M:%S.%f%z',
    '%Y-%m-%dT%H:%M:%S%z'
]


# ==================
#      Classes
# ==================
class ValidatedDatetime(datetime):
    @classmethod
    def __get_validators__(cls):
        yield cls.validator

    @classmethod
    def validator(cls, dt: Optional[Union[str, datetime]]) -> Optional[datetime]:
        if dt and not isinstance(dt, datetime):
            return parse_datetime(dt)
        return dt


# ==================
#     Functions
# ==================
def parse_datetime(dt: str) -> datetime:
    for fmt in DATETIME_FMTS:
        try:
            return datetime.strptime(dt, fmt)
        except ValueError:
            pass
    raise ValueError(f'Time data \'{dt}\' matches no known formats.')


def process_errors(response: dict):
    if 'ErrorCode' in response:
        return errors.EXCEPTIONS[response['ErrorCode']](response['Message'])

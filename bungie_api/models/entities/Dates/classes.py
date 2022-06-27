from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime


__all__ = [
    'DateRange',
]


class DateRange(BaseModel):
    start: ValidatedDatetime
    end: ValidatedDatetime

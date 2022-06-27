from typing import (
    Optional,
)

from arya_api_framework import BaseModel

from ...utils import ValidatedDatetime


__all__ = [
    'GetApplicationApiUsage',
]


class GetApplicationApiUsage(BaseModel):
    start: Optional[ValidatedDatetime]
    end: Optional[ValidatedDatetime]

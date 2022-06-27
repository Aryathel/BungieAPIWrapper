from arya_api_framework import BaseModel

from .enums import IgnoreStatus


__all__ = [
    'IgnoreResponse',
]


class IgnoreResponse(BaseModel):
    isIgnored: bool
    ignoreFlags: IgnoreStatus

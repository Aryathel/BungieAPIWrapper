from arya_api_framework import BaseModel

from ....Ignores.classes import IgnoreResponse


__all__ = [
    'TagResponse'
]


class TagResponse(BaseModel):
    tagText: str
    ignoreStatus: IgnoreResponse

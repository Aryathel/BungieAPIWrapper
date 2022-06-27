from arya_api_framework import BaseModel


from ..Exceptions.enums import PlatformErrorCodes


__all__ = [
    'EntityActionResult',
]


class EntityActionResult(BaseModel):
    entityId: int
    result: PlatformErrorCodes

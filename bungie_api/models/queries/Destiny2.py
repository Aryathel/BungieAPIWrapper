from typing import (
    Iterable,
    Optional,
    Union,
)

from arya_api_framework import BaseModel
from pydantic import Field

from ..entities import Destiny


__all__ = [
    'GetLinkedProfiles',
]


ComponentType = Union[int, str, Destiny.DestinyComponentType]
ComponentListType = Iterable[ComponentType]


class GetLinkedProfiles(BaseModel):
    getAllMemberships: Optional[bool]


class GetProfile(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')

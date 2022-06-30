from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from .....utils import ValidatedDatetime
from ...enums import BungieMembershipType
from .enums import AwaType


__all__ = [
    'AwaPermissionRequested',
    'AwaInitializeResponse',
    'AwaUserResponse',
    'AwaAuthorizationResult',
]


class AwaPermissionRequested(BaseModel):
    type: AwaType
    affectedItemId: Optional[int]
    membershipType: BungieMembershipType
    characterId: Optional[int]


class AwaInitializeResponse(BaseModel):
    correlationId: str
    sentToSelf: bool


class AwaUserResponse(BaseModel):
    selection: int
    correlationId: str
    nonce: List[str]


class AwaAuthorizationResult(BaseModel):
    userSelection: int
    responseReason: int
    developerNote: str
    actionToken: str
    maximumNumberOfUsers: int
    validUntil: Optional[ValidatedDatetime]
    type: AwaType
    membershipType: BungieMembershipType

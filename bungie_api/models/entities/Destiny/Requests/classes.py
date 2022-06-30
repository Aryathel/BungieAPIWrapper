from typing import Optional

from arya_api_framework import BaseModel

from ...enums import BungieMembershipType


__all__ = [
    'DestinyItemTransferRequest',
]


class DestinyItemTransferRequest(BaseModel):
    itemReferenceHash: int
    stackSize: Optional[int]
    transferToVault: bool
    itemId: int
    characterId: int
    membershipType: BungieMembershipType

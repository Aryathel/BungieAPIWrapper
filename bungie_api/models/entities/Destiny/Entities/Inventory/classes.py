from typing import List

from arya_api_framework import BaseModel

from .. import Items


__all__ = [
    'DestinyInventoryComponent',
]


class DestinyInventoryComponent(BaseModel):
    items: List[Items.DestinyItemComponent]

from typing import (
    List,
    Mapping,
)

from arya_api_framework import BaseModel

from ... import Sockets


__all__ = [
    'DestinyPlugSetsComponent',
]


class DestinyPlugSetsComponent(BaseModel):
    plugs: Mapping[int, List[Sockets.DestinyItemPlug]]

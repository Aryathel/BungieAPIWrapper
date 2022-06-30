from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel


__all__ = [
    'DestinyReportOffensePgcrRequest',
]


class DestinyReportOffensePgcrRequest(BaseModel):
    reasonCategoryHashes: List[int]
    reasonHashes: Optional[List[int]]
    offendingCharacterId: int

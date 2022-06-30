from typing import Optional

from arya_api_framework import BaseModel


__all__ = [
    'GetAvailableClanFireteams',
    'SearchPublicAvailableClanFireteams',
    'GetMyClanFireteams',
]


class GetAvailableClanFireteams(BaseModel):
    langFilter: Optional[str]


class SearchPublicAvailableClanFireteams(BaseModel):
    langFilter: Optional[str]


class GetMyClanFireteams(BaseModel):
    groupFilter: Optional[bool]
    langFilter: Optional[str]

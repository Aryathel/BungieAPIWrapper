from datetime import datetime
from typing import (
    Iterable,
    Optional,
    Union,
)

from arya_api_framework import BaseModel
from pydantic import (
    Field,
    validator,
)

from ...utils import parse_datetime
from ..entities import Destiny


__all__ = [
    'GetLinkedProfiles',
    'GetProfile',
    'GetCharacter',
    'GetItem',
    'GetVendors',
    'GetVendor',
    'GetPublicVendors',
    'GetCollectibleNodeDetails',
    'GetClanLeaderboards',
    'GetClanAggregateStats',
    'SearchDestinyEntities',
    'GetHistoricalStats',
    'GetHistoricalStatsForAccount',
    'GetActivityHistory',
]


ComponentType = Union[int, str, Destiny.DestinyComponentType]
ComponentListType = Iterable[ComponentType]


class GetLinkedProfiles(BaseModel):
    getAllMemberships: Optional[bool]


class GetProfile(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetCharacter(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetItem(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetVendors(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')
    filter: Destiny.DestinyVendorFilter


class GetVendor(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetPublicVendors(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetCollectibleNodeDetails(BaseModel):
    components: Destiny.DestinyComponentType = Field(..., type='int_list_str')


class GetClanLeaderboards(BaseModel):
    maxtop: Optional[int]
    modes: Optional[Destiny.HistoricalStats.Definitions.DestinyActivityModeType] = Field(type='str_list_str')
    statid: Optional[str]


class GetClanAggregateStats(BaseModel):
    modes: Optional[Destiny.HistoricalStats.Definitions.DestinyActivityModeType] = Field(type='str_list_str')


class SearchDestinyEntities(BaseModel):
    page: Optional[int]


class GetHistoricalStats(BaseModel):
    dayend: Optional[str]
    daystart: Optional[str]
    groups: Optional[Destiny.HistoricalStats.Definitions.DestinyStatsGroupType] = Field(type='str_list_str')
    modes: Optional[Destiny.HistoricalStats.Definitions.DestinyActivityModeType] = Field(type='str_list_str')
    periodType: Optional[Destiny.HistoricalStats.Definitions.PeriodType] = Field(type='str')

    @validator('dayend', 'daystart', pre=True)
    def validate_datetime(cls, dt: Union[str, datetime]) -> Optional[str]:
        if dt is None:
            return

        if isinstance(dt, str):
            dt = parse_datetime(dt)
        return dt.strftime('%Y-%m-%d')


class GetHistoricalStatsForAccount(BaseModel):
    groups: Optional[Destiny.HistoricalStats.Definitions.DestinyStatsGroupType] = Field(type='str_list_str')


class GetActivityHistory(BaseModel):
    count: Optional[int]
    mode: Optional[Destiny.HistoricalStats.Definitions.DestinyActivityModeType]
    page: Optional[int]

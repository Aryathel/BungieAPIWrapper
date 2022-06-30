from typing import (
    ForwardRef,
    List,
    Optional,
    Union,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from ...entities import (
    Content,
    Destiny,
)
from .enums import TrendingEntryType


__all__ = [
    'TrendingCategory',
    'TrendingCategories',
    'TrendingEntry',
    'TrendingEntryNews',
    'TrendingEntrySupportArticle',
    'TrendingEntryDestinyItem',
    'TrendingEntryDestinyActivity',
    'TrendingEntryDestinyRitual',
    'TrendingEntryCommunityCreation',
    'TrendingDetail',
]


SearchResultOfTrendingEntry = ForwardRef('entities.SearchResultOfTrendingEntry')


class TrendingCategory(BaseModel):
    categoryName: str
    entries: SearchResultOfTrendingEntry
    categoryId: str


class TrendingCategories(BaseModel):
    categories: List[TrendingCategory]


class TrendingEntry(BaseModel):
    weight: float
    isFeatured: bool
    identifier: Union[int, str]
    entityType: TrendingEntryType
    displayName: str
    tagline: str
    image: str
    startDate: Optional[ValidatedDatetime]
    endDate: Optional[ValidatedDatetime]
    link: str
    webmVideo: Optional[str]
    mp4Video: Optional[str]
    featureImage: Optional[str]
    items: Optional[List['TrendingEntry']]
    creationDate: Optional[ValidatedDatetime]


class TrendingEntryNews(BaseModel):
    article: Content.ContentItemPublicContract


class TrendingEntrySupportArticle(BaseModel):
    article: Content.ContentItemPublicContract


class TrendingEntryDestinyItem(BaseModel):
    itemHash: int


class TrendingEntryDestinyActivity(BaseModel):
    activityHash: int
    status: Destiny.Activities.DestinyPublicActivityStatus


class TrendingEntryDestinyRitual(BaseModel):
    image: str
    icon: str
    title: str
    subtitle: str
    dateStart: Optional[ValidatedDatetime]
    dateEnd: Optional[ValidatedDatetime]
    milestoneDetails: Destiny.Milestones.DestinyPublicMilestone
    eventContent: Destiny.Milestones.DestinyMilestoneContent


class TrendingEntryCommunityCreation(BaseModel):
    media: str
    title: str
    author: str
    authorMembershipId: int
    postId: int
    body: Optional[str]
    upvotes: int


class TrendingDetail(BaseModel):
    identifier: Union[int, str]
    entityType: TrendingEntryType
    news: Optional[TrendingEntryNews]
    support: Optional[TrendingEntrySupportArticle]
    destinyItem: Optional[TrendingEntryDestinyItem]
    destinyActivity: Optional[TrendingEntryDestinyActivity]
    destinyRitual: Optional[TrendingEntryDestinyRitual]
    creation: Optional[TrendingEntryCommunityCreation]


from ... import entities

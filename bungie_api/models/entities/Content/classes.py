from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from arya_api_framework import BaseModel


from ....utils import ValidatedDatetime
from ..User.classes import GeneralUser
from ..Queries.classes import PagedQuery


__all__ = [
    'ContentItemPublicContract',
    'CommentSummary',
    'ContentRepresentation',
    'SearchResultOfContentItemPublicContract',
]


class ContentRepresentation(BaseModel):
    name: str
    path: str
    validationString: str


class CommentSummary(BaseModel):
    topicId: int
    commentCount: int


class ContentItemPublicContract(BaseModel):
    contentId: int
    cType: str
    cmsPath: str
    creationDate: ValidatedDatetime
    modifyDate: ValidatedDatetime
    allowComments: bool
    hasAgeGate: bool
    minimumAge: int
    ratingImagePath: str
    author: GeneralUser
    autoEnglishPropertyFallback: bool
    properties: Dict[str, Any]
    representations: List[ContentRepresentation]
    tags: List[str]
    commentSummary: Optional[CommentSummary]


class SearchResultOfContentItemPublicContract(BaseModel):
    results: List[ContentItemPublicContract]
    totalResults: int
    hasMore: bool
    query: PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool

from typing import (
    List,
    Optional,
    Union,
)

from arya_api_framework import BaseModel
from pydantic import validator


__all__ = [
    'GetTopicsPaged',
    'GetCoreTopicsPaged',
    'GetPostsThreadedPaged',
    'GetPostsThreadedPagedFromChild',
    'GetPostAndParent',
    'GetPostAndParentAwaitingApproval',
    'GetForumTagSuggestions',
]


class GetTopicsPaged(BaseModel):
    locales: Optional[str]
    tagstring: Optional[str]

    @validator('locales', pre=True)
    def validate_locales(cls, locales: Optional[Union[str, List[str]]]) -> Optional[str]:
        if locales is None:
            return
        if isinstance(locales, str):
            return locales
        return ','.join(locales)


class GetCoreTopicsPaged(BaseModel):
    locales: Optional[str]

    @validator('locales', pre=True)
    def validate_locales(cls, locales: Optional[Union[str, List[str]]]) -> Optional[str]:
        if locales is None:
            return
        if isinstance(locales, str):
            return locales
        return ','.join(locales)


class GetPostsThreadedPaged(BaseModel):
    showbanned: Optional[bool]

    @validator('showbanned')
    def blank_if_false(cls, val: Optional[bool]) -> Optional[bool]:
        return val if val else None


class GetPostsThreadedPagedFromChild(BaseModel):
    showbanned: Optional[bool]

    @validator('showbanned')
    def blank_if_false(cls, val: Optional[bool]) -> Optional[bool]:
        return val if val else None


class GetPostAndParent(BaseModel):
    showbanned: Optional[bool]

    @validator('showbanned')
    def blank_if_false(cls, val: Optional[bool]) -> Optional[bool]:
        return val if val else None


class GetPostAndParentAwaitingApproval(BaseModel):
    showbanned: Optional[bool]

    @validator('showbanned')
    def blank_if_false(cls, val: Optional[bool]) -> Optional[bool]:
        return val if val else None


class GetForumTagSuggestions(BaseModel):
    partialtag: str

from typing import Optional

from arya_api_framework import BaseModel


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
    locales: str
    tagstring: Optional[str]


class GetCoreTopicsPaged(BaseModel):
    locales: str


class GetPostsThreadedPaged(BaseModel):
    showbanned: Optional[bool]


class GetPostsThreadedPagedFromChild(BaseModel):
    showbanned: Optional[bool]


class GetPostAndParent(BaseModel):
    showbanned: Optional[bool]


class GetPostAndParentAwaitingApproval(BaseModel):
    showbanned: Optional[bool]


class GetForumTagSuggestions(BaseModel):
    partialtag: str

from typing import Optional

from arya_api_framework import BaseModel


__all__ = [
    'GetContentById',
    'GetContentByTagAndType',
    'SearchContentWithText',
    'SearchContentByTagAndType',
]


class GetContentById(BaseModel):
    head: bool


class GetContentByTagAndType(BaseModel):
    head: bool


class SearchContentWithText(BaseModel):
    ctype: str
    currentpage: Optional[int]
    head: Optional[bool]
    searchtext: Optional[str]
    source: Optional[str]
    tag: Optional[str]


class SearchContentByTagAndType(BaseModel):
    currentpage: Optional[int]
    head: Optional[bool]
    itemsperpage: Optional[bool]

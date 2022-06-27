from typing import Optional

from .. import entities
from .framework import BaseResponse, PaginatedBaseResponse


__all__ = [
    'GetContentType',
    'GetContentById',
    'GetContentByTagAndType',
    'SearchContentWithText',
    'SearchContentByTagAndType',
]


class GetContentType(BaseResponse):
    Response: Optional[entities.Content.Models.ContentTypeDescription]


class GetContentById(BaseResponse):
    Response: entities.Content.ContentItemPublicContract


class GetContentByTagAndType(BaseResponse):
    Response: entities.Content.ContentItemPublicContract


class SearchContentWithText(PaginatedBaseResponse):
    Response: entities.Content.SearchResultOfContentItemPublicContract

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def previous(self) -> None:
        return


class SearchContentByTagAndType(PaginatedBaseResponse):
    Response: entities.Content.SearchResultOfContentItemPublicContract

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def previous(self) -> None:
        return

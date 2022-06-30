from typing import Optional

from ..entities import (
    Trending,
    SearchResultOfTrendingEntry,
)
from .framework import BaseResponse, PaginatedBaseResponse


__all__ = [
    'GetTrendingCategories',
    'GetTrendingCategory',
    'GetTrendingEntryDetail',
]


class GetTrendingCategories(BaseResponse):
    Response: Trending.TrendingCategories


class GetTrendingCategory(PaginatedBaseResponse):
    Response: SearchResultOfTrendingEntry

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def start(self) -> None:
        return


class GetTrendingEntryDetail(BaseResponse):
    Response: Trending.TrendingDetail

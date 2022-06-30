from typing import Optional

from ..entities import Forum
from .framework import PaginatedBaseResponse


__all__ = [
    'GetCommunityContent',
]


class GetCommunityContent(PaginatedBaseResponse):
    Response: Forum.PostSearchResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage

    @property
    def previous(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def start(self) -> None:
        return

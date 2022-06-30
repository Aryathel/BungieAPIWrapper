from typing import Optional

from ..entities import (
    SearchResultOfFireteamSummary,
    Fireteam,
)
from .framework import BaseResponse, PaginatedBaseResponse


__all__ = [
    'GetActivePrivateClanFireteamCount',
    'GetAvailableClanFireteams',
    'SearchPublicAvailableClanFireteams',
    'GetMyClanFireteams',
]


class GetActivePrivateClanFireteamCount(BaseResponse):
    Response: int


class GetAvailableClanFireteams(PaginatedBaseResponse):
    Response: SearchResultOfFireteamSummary

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


class SearchPublicAvailableClanFireteams(PaginatedBaseResponse):
    Response: SearchResultOfFireteamSummary

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


class GetMyClanFireteams(PaginatedBaseResponse):
    Response: SearchResultOfFireteamSummary

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


class GetClanFireteam(BaseResponse):
    Response: Fireteam.FireteamResponse

from typing import (
    List,
    Optional,
)

from .. import entities
from .framework import PaginatedBaseResponse, BaseResponse


__all__ = [
    'GetTopicsPaged',
    'GetCoreTopicsPaged',
    'GetPostsThreadedPaged',
    'GetPostsThreadedPagedFromChild',
    'GetPostAndParent',
    'GetPostAndParentAwaitingApproval',
    'GetTopicForContent',
    'GetPoll',
]


class GetTopicsPaged(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetCoreTopicsPaged(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetPostsThreadedPaged(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetPostsThreadedPagedFromChild(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetPostAndParent(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetPostAndParentAwaitingApproval(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetTopicForContent(BaseResponse):
    Response: Optional[int]


class GetForumTagSuggestions(BaseResponse):
    Response: List[entities.Tags.Models.Contracts.TagResponse]


class GetPoll(PaginatedBaseResponse):
    Response: entities.Forum.PostSearchResponse

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


class GetRecruitmentThreadSummaries(BaseResponse):
    Response: List[entities.Forum.ForumRecruitmentDetail]

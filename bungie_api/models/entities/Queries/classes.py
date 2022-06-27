from typing import (
    Optional,
)

from arya_api_framework import BaseModel
from pydantic import Extra


__all__ = [
    'PagedQuery',
]


class PagedQuery(BaseModel):
    itemsPerPage: int
    currentPage: int
    requestContinuationToken: Optional[str]

    class Config:
        extra = Extra.allow

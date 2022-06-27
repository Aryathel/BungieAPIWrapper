from abc import ABC
from typing import (
    Any,
    Dict,
    Optional,
)

from arya_api_framework import (
    Response,
    PaginatedResponse,
)

from ..entities.Exceptions import PlatformErrorCodes

__all__ = [
    'BaseResponse',
    'PaginatedBaseResponse'
]


class BaseResponse(Response):
    Response: Any
    ErrorCode: PlatformErrorCodes
    ThrottleSeconds: int
    ErrorStatus: str
    Message: str
    MessageData: Dict[str, str]
    DetailedErrorTrace: Optional[str]


class PaginatedBaseResponse(PaginatedResponse, ABC):
    Response: Any
    ErrorCode: PlatformErrorCodes
    ThrottleSeconds: int
    ErrorStatus: str
    Message: str
    MessageData: Dict[str, str]
    DetailedErrorTrace: Optional[str]

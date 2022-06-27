from typing import List

from ..entities import Applications
from .framework import BaseResponse


__all__ = [
    'GetApplicationApiUsage',
    'GetBungieApplications',
]


class GetApplicationApiUsage(BaseResponse):
    Response: List[Applications.ApiUsage]


class GetBungieApplications(BaseResponse):
    Response: List[Applications.Application]

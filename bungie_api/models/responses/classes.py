from typing import (
    List,
    Mapping,
)

from ..entities import (
    Common,
    GlobalAlert,
)
from .framework import BaseResponse


__all__ = [
    'GetAvailableLocales',
    'GetCommonSettings',
    'GetUserSystemOverrides',
    'GetGlobalAlerts',
]


class GetAvailableLocales(BaseResponse):
    Response: Mapping[str, str]


class GetCommonSettings(BaseResponse):
    Response: Common.Models.CoreSettingsConfiguration


class GetUserSystemOverrides(BaseResponse):
    Response: Mapping[str, Common.Models.CoreSystem]


class GetGlobalAlerts(BaseResponse):
    Response: List[GlobalAlert]

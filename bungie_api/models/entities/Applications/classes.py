from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from .. import User
from .enums import (
    ApplicationScopes,
    ApplicationStatus,
    DeveloperRole,
)

__all__ = [
    'ApiUsage',
    'Series',
    'Datapoint',
    'Application',
    'ApplicationDeveloper',
]


# ==================
#       Models
# ==================
class Datapoint(BaseModel):
    time: ValidatedDatetime
    count: float


class Series(BaseModel):
    datapoints: List[Datapoint]
    target: str


class ApiUsage(BaseModel):
    apiCalls: List[Series]
    throttledRequests: List[Series]


class ApplicationDeveloper(BaseModel):
    role: DeveloperRole
    apiEulaVersion: int
    user: User.UserInfoCard


class Application(BaseModel):
    applicationId: int
    name: str
    redirectUrl: str
    link: str
    scope: ApplicationScopes
    origin: Optional[str]
    status: ApplicationStatus
    creationDate: ValidatedDatetime
    statusChanged: ValidatedDatetime
    firstPublished: ValidatedDatetime
    team: List[ApplicationDeveloper]
    overrideAuthorizeViewName: Optional[str]

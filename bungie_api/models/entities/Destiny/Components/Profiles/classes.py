from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ... import (
    DestinyPartyMemberStates,
    DestinyGamePrivacySetting,
    DestinyJoinClosedReasons,
)


__all__ = [
    'DestinyProfileProgressionComponent',
    'DestinyProfileTransitoryPartyMember',
    'DestinyProfileTransitoryCurrentActivity',
    'DestinyProfileTransitoryJoinability',
    'DestinyProfileTransitoryTrackingEntry',
    'DestinyProfileTransitoryComponent',
]


class DestinyProfileProgressionComponent(BaseModel):
    checklist: Mapping[int, Mapping[int, bool]]


class DestinyProfileTransitoryPartyMember(BaseModel):
    membershipId: int
    emblemHash: int
    displayName: str
    status: DestinyPartyMemberStates


class DestinyProfileTransitoryCurrentActivity(BaseModel):
    startTime: Optional[ValidatedDatetime]
    endTime: Optional[ValidatedDatetime]
    score: float
    highestOpposingFactionScore: float
    numberOfOpponents: int
    numberOfPlayers: int


class DestinyProfileTransitoryJoinability(BaseModel):
    openSlots: int
    privacySetting: DestinyGamePrivacySetting
    closedReasons: DestinyJoinClosedReasons


class DestinyProfileTransitoryTrackingEntry(BaseModel):
    locationHash: Optional[int]
    itemHash: Optional[int]
    objectiveHash: Optional[int]
    activityHash: Optional[int]
    questlineItemHash: Optional[int]
    trackedDate: Optional[ValidatedDatetime]


class DestinyProfileTransitoryComponent(BaseModel):
    partyMembers: List[DestinyProfileTransitoryPartyMember]
    currentActivity: DestinyProfileTransitoryCurrentActivity
    joinability: DestinyProfileTransitoryJoinability
    tracking: List[DestinyProfileTransitoryTrackingEntry]
    lastOrbitedDestinationHash: Optional[int]

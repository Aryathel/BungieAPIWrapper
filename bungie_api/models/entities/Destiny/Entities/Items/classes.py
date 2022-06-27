from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ... import (
    ItemBindStatus,
    ItemLocation,
    TransferStatuses,
    ItemState,
    Perks,
    Quests,
    DamageType,
    TierType,
    DestinyStat,
    EquipFailureReason,
    DestinyBreakerType,
    DestinyEnergyType,
    DestinyProgression,
    DestinyTalentNode,
)


__all__ = [
    'DestinyItemPerksComponent',
    'DestinyItemComponent',
    'DestinyItemObjectivesComponent',
    'DestinyItemInstanceComponent',
    'DestinyItemInstanceEnergy',
    'DestinyItemRenderComponent',
    'DestinyItemStatsComponent',
    'DestinyItemSocketState',
    'DestinyItemSocketsComponent',
    'DestinyItemTalentGridComponent',
]


class DestinyItemComponent(BaseModel):
    itemHash: int
    itemInstanceId: Optional[int]
    quantity: int
    bindStatus: ItemBindStatus
    location: ItemLocation
    bucketHash: int
    transferStatus: TransferStatuses
    lockable: bool
    state: ItemState
    overrideStyleItemHash: Optional[int]
    expirationDate: Optional[ValidatedDatetime]
    isWrapper: bool
    tooltipNotificationIndexes: Optional[List[int]]
    metricHash: Optional[int]
    metricObjective: Optional[Quests.DestinyObjectiveProgress]
    versionNumber: Optional[int]
    itemValueVisibility: Optional[List[bool]]
    dismantlePermission: int


class DestinyItemPerksComponent(BaseModel):
    perks: List[Perks.DestinyPerkReference]


class DestinyItemObjectivesComponent(BaseModel):
    objectives: List[Quests.DestinyObjectiveProgress]
    flavorObjective: Optional[Quests.DestinyObjectiveProgress]
    dateCompleted: Optional[ValidatedDatetime]


class DestinyItemInstanceEnergy(BaseModel):
    energyTypeHash: int
    energyType: DestinyEnergyType
    energyCapacity: int
    energyUsed: int
    energyUnused: int


class DestinyItemInstanceComponent(BaseModel):
    damageType: DamageType
    damageTypeHash: Optional[int]
    primaryStat: Optional[DestinyStat]
    itemLevel: int
    quality: int
    isEquipped: bool
    canEquip: bool
    equipRequiredLevel: int
    unlockHashesRequiredToEquip: List[int]
    cannotEquipReason: EquipFailureReason
    breakerType: Optional[DestinyBreakerType]
    breakerTypeHash: Optional[int]
    energy: Optional[DestinyItemInstanceEnergy]


class DestinyItemRenderComponent(BaseModel):
    useCustomDyes: bool
    artRegions: Mapping[int, int]


class DestinyItemStatsComponent(BaseModel):
    stats: Mapping[int, DestinyStat]


class DestinyItemSocketState(BaseModel):
    plugHash: Optional[int]
    isEnabled: bool
    isVisible: bool
    enableFailIndexes: Optional[List[int]]


class DestinyItemSocketsComponent(BaseModel):
    sockets: List[DestinyItemSocketState]


class DestinyItemTalentGridComponent(BaseModel):
    talentGridHash: int
    nodes: List[DestinyTalentNode]
    isGridComplete: bool
    gridProgression: Optional[DestinyProgression]

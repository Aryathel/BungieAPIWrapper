from typing import (
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel


from ...enums import (
    DestinyScope,
    DestinyRecordValueStyle,
    DestinyPresentationNodeType,
    DestinyRecordToastStyle,
    DestinyGender,
)
from .. import (
    Common,
    Presentation,
)


DestinyItemQuantity = ForwardRef('classes.DestinyItemQuantity')


__all__ = [
    'DestinyRecordTitleBlock',
    'DestinyRecordCompletionBlock',
    'SchemaRecordStateBlock',
    'DestinyRecordExpirationBlock',
    'DestinyRecordIntervalObjective',
    'DestinyRecordIntervalRewards',
    'DestinyRecordIntervalBlock',
    'DestinyRecordDefinition',
]


class DestinyRecordTitleBlock(BaseModel):
    hasTitle: bool
    titlesByGender: Optional[Mapping[DestinyGender, str]]
    titlesByGenderHash: Optional[Mapping[int, str]]
    gildingTrackingRecordHash: Optional[int]


class DestinyRecordCompletionBlock(BaseModel):
    partialCompletionObjectiveCountThreshold: int
    ScoreValue: int
    shouldFireToast: bool
    toastStyle: DestinyRecordToastStyle


class SchemaRecordStateBlock(BaseModel):
    featuredPriority: int
    obscuredString: Optional[str]
    featuredPriority: int
    completeUnlockHash: int
    claimedUnlockHash: int
    toastStyle: Optional[DestinyRecordToastStyle]
    completedCounterUnlockValueHash: int


class DestinyRecordExpirationBlock(BaseModel):
    hasExpiration: bool
    description: str
    icon: Optional[str]


class DestinyRecordIntervalObjective(BaseModel):
    intervalObjectiveHash: int
    intervalScoreValue: int


class DestinyRecordIntervalRewards(BaseModel):
    intervalRewardItems: List[DestinyItemQuantity]


class DestinyRecordIntervalBlock(BaseModel):
    intervalObjectives: List[DestinyRecordIntervalObjective]
    intervalRewards: List[DestinyRecordIntervalRewards]
    originalObjectiveArrayInsertionIndex: int
    isIntervalVersionedFromNormalRecord: bool


class DestinyRecordDefinition(BaseModel):
    displayProperties: Common.DestinyDisplayPropertiesDefinition
    scope: DestinyScope
    presentationInfo: Optional[Presentation.DestinyPresentationChildBlock]
    loreHash: Optional[int]
    objectiveHashes: List[int]
    recordValueStyle: DestinyRecordValueStyle
    forTitleGilding: bool
    shouldShowLargeIcons: bool
    titleInfo: DestinyRecordTitleBlock
    completionInfo: DestinyRecordCompletionBlock
    stateInfo: SchemaRecordStateBlock
    requirements: Presentation.DestinyPresentationNodeRequirementsBlock
    expirationInfo: DestinyRecordExpirationBlock
    intervalInfo: DestinyRecordIntervalBlock
    rewardItems: List[DestinyItemQuantity]
    presentationNodeType: DestinyPresentationNodeType
    traitIds: List[str]
    traitHashes: List[int]
    parentNodeHashes: List[int]
    hash: int
    index: int
    redacted: bool
    anyRewardHasConditionalVisibility: bool
    blacklisted: bool


from ... import classes

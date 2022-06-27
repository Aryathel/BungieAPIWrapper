from typing import List, Optional

from arya_api_framework import BaseModel

from ...enums import (
    PlugUiStyles,
    PlugAvailabilityMode,
    DestinyEnergyType
)


__all__ = [
    'DestinyPlugRuleDefinition',
    'DestinyParentItemOverride',
    'DestinyEnergyCapacityEntry',
    'DestinyEnergyCostEntry',
    'DestinyItemPlugDefinition',
    'DestinyDerivedItemDefinition',
    'DestinyDerivedItemCategoryDefinition',
]


class DestinyPlugRuleDefinition(BaseModel):
    failureMessage: str


class DestinyParentItemOverride(BaseModel):
    additionalEquipRequirementsDisplayStrings: List[str]
    pipIcon: str


class DestinyEnergyCapacityEntry(BaseModel):
    capacityValue: int
    energyTypeHash: int
    energyType: DestinyEnergyType


class DestinyEnergyCostEntry(BaseModel):
    energyCost: int
    energyTypeHash: int
    energyType: DestinyEnergyType


class DestinyItemPlugDefinition(BaseModel):
    insertionRules: List[DestinyPlugRuleDefinition]
    plugCategoryIdentifier: str
    plugCategoryHash: int
    onActionRecreateSelf: bool
    insertionMaterialRequirementHash: int
    previewItemOverrideHash: int
    enabledMaterialRequirementHash: int
    enabledRules: List[DestinyPlugRuleDefinition]
    uiPlugLabel: str
    plugStyle: PlugUiStyles
    plugAvailability: PlugAvailabilityMode
    alternateUiPlugLabel: str
    alternatePlugStyle: PlugUiStyles
    isDummyPlug: bool
    parentItemOverride: DestinyParentItemOverride
    energyCapacity: DestinyEnergyCapacityEntry
    energyCost: DestinyEnergyCostEntry


class DestinyDerivedItemDefinition(BaseModel):
    itemHash: Optional[int]
    itemName: str
    itemDetail: str
    itemDescription: str
    iconPath: str
    vendorItemIndex: int


class DestinyDerivedItemCategoryDefinition(BaseModel):
    categoryDescription: str
    items: List[DestinyDerivedItemDefinition]

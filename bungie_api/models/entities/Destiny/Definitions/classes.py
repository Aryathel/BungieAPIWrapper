from typing import (
    Dict,
    ForwardRef,
    List,
    Optional,
)

from arya_api_framework import BaseModel
from pydantic import Extra

from ... import Links
from .. import Misc
from ..enums import (
    SpecialItemType,
    DestinyItemType,
    DestinyItemSubType,
    DamageType,
    TierType,
    DestinyBreakerType,
    DestinyClass,
    ItemPerkVisibility,
)
from . import (
    Common,
    Animations,
    Items,
    Sources,
)


DestinyItemQuantity = ForwardRef('Destiny.DestinyItemQuantity')
DyeReference = ForwardRef('Destiny.DyeReference')
SearchResultOfDestinyEntitySearchResultItem = ForwardRef('entities.SearchResultOfDestinyEntitySearchResultItem')


__all__ = [
    'DestinyItemTooltipNotification',
    'DestinyItemActionRequiredItemDefinition',
    'DestinyProgressionRewardDefinition',
    'DestinyItemActionBlockDefinition',
    'DestinyItemCraftingBlockBonusPlugDefinition',
    'DestinyItemCraftingBlockDefinition',
    'DestinyItemInventoryBlockDefinition',
    'DestinyItemSetBlockEntryDefinition',
    'DestinyItemSetBlockDefinition',
    'DestinyInventoryItemStatDefinition',
    'DestinyItemStatBlockDefinition',
    'DestinyEquippingBlockDefinition',
    'DestinyGearArtArrangementReference',
    'DestinyItemTranslationBlockDefinition',
    'DestinyItemPreviewBlockDefinition',
    'DestinyItemVersionDefinition',
    'DestinyItemQualityBlockDefinition',
    'DestinyItemValueBlockDefinition',
    'DestinyItemVendorSourceReference',
    'DestinyItemSourceBlockDefinition',
    'DestinyObjectiveDisplayProperties',
    'DestinyItemObjectiveBlockDefinition',
    'DestinyItemMetricBlockDefinition',
    'DestinyItemGearsetBlockDefinition',
    'DestinyItemSackBlockDefinition',
    'DestinyItemSocketEntryPlugItemDefinition',
    'DestinyItemSocketEntryDefinition',
    'DestinyItemIntrinsicSocketEntryDefinition',
    'DestinyItemSocketCategoryDefinition',
    'DestinyItemSocketBlockDefinition',
    'DestinyItemSummaryBlockDefinition',
    'DestinyItemTalentGridBlockDefinition',
    'DestinyItemInvestmentStatDefinition',
    'DestinyItemPerkEntryDefinition',
    'DestinyInventoryItemDefinition',
    'DestinyDefinition',
    'DestinyMaterialRequirement',
    'DestinyEntitySearchResult',
    'DestinyEntitySearchResultItem',
]


class DestinyItemTooltipNotification(BaseModel):
    displayString: str
    displayStyle: str


class DestinyItemActionRequiredItemDefinition(BaseModel):
    count: int
    itemHash: int
    deleteOnAction: bool


class DestinyProgressionRewardDefinition(BaseModel):
    progressionMappingHash: int
    amount: int
    applyThrottles: bool


class DestinyItemActionBlockDefinition(BaseModel):
    verbName: str
    verbDescription: str
    isPositive: bool
    overlayScreenName: str
    overlayIcon: str
    requiredCooldownSeconds: int
    requiredItems: List[DestinyItemActionRequiredItemDefinition]
    progressionRewards: List[DestinyProgressionRewardDefinition]
    actionTypeLabel: str
    requiredLocation: str
    requiredCooldownHash: int
    deleteOnAction: bool
    consumeEntireStack: bool
    useOnAcquire: bool


class DestinyItemCraftingBlockBonusPlugDefinition(BaseModel):
    socketTypeHash: int
    plugItemHash: int


class DestinyItemCraftingBlockDefinition(BaseModel):
    outputItemHash: int
    requiredSocketTypeHashes: List[int]
    failedRequirementStrings: List[str]
    baseMaterialRequirements: Optional[int]
    bonusPlugs: List[DestinyItemCraftingBlockBonusPlugDefinition]


class DestinyItemInventoryBlockDefinition(BaseModel):
    stackUniqueLabel: str
    maxStackSize: int
    bucketTypeHash: int
    recoveryBucketTypeHash: int
    tierTypeHash: int
    isInstanceItem: bool
    tierTypeName: str
    tierType: TierType
    expirationTooltip: str
    expiredInActivityMessage: str
    expiredInOrbitMessage: str
    suppressExpirationWhenObjectivesComplete: bool
    recipeItemHash: Optional[int]


class DestinyItemSetBlockEntryDefinition(BaseModel):
    trackingValue: int
    itemHash: int


class DestinyItemSetBlockDefinition(BaseModel):
    itemList: List[DestinyItemSetBlockEntryDefinition]
    requireOrderedSetItemAdd: bool
    setIsFeatured: bool
    setType: str
    questLineName: str
    questLineDescription: str
    questStepSummary: str


class DestinyInventoryItemStatDefinition(BaseModel):
    statHash: int
    value: int
    minimum: int
    maximum: int
    displayMaximum: Optional[int]


class DestinyItemStatBlockDefinition(BaseModel):
    disablePrimaryStatDisplay: bool
    statGroupHash: Optional[int]
    stats: Dict[int, DestinyInventoryItemStatDefinition]
    hasDisplayableStats: bool
    primaryBaseStatHash: int


class DestinyEquippingBlockDefinition(BaseModel):
    gearsetItemHash: Optional[int]
    uniqueLabel: str
    uniqueLabelHash: int
    equipmentSlotTypeHash: int
    attributes: int
    ammoType: int
    displayStrings: List[str]


class DestinyGearArtArrangementReference(BaseModel):
    classHash: int
    artArrangementHash: int


class DestinyItemTranslationBlockDefinition(BaseModel):
    weaponPatternIdentifier: str
    weaponPatternHash: int
    defaultDyes: List[DyeReference]
    lockedDyes: List[DyeReference]
    customDyes: List[DyeReference]
    arrangements: List[DestinyGearArtArrangementReference]
    hasGeometry: bool


class DestinyItemPreviewBlockDefinition(BaseModel):
    screenStyle: str
    previewVendorHash: int
    artifactHash: Optional[int]
    previewActionString: str
    derivedItemCategories: List[Items.DestinyDerivedItemCategoryDefinition]


class DestinyItemVersionDefinition(BaseModel):
    powerCapHash: int


class DestinyItemQualityBlockDefinition(BaseModel):
    itemLevels: List[int]
    qualityLevel: int
    infusionCategoryName: str
    infusionCategoryHash: int
    infusionCategoryHashes: List[int]
    progressionLevelRequirementHash: int
    currentVersion: int
    versions: List[DestinyItemVersionDefinition]
    displayVersionWatermarkIcons: List[str]


class DestinyItemValueBlockDefinition(BaseModel):
    itemValue: List[DestinyItemQuantity]
    valueDescription: str


class DestinyItemVendorSourceReference(BaseModel):
    vendorHash: int
    vendorItemIndexes: List[int]


class DestinyItemSourceBlockDefinition(BaseModel):
    sourceHashes: List[int]
    sources: List[Sources.DestinyItemSourceDefinition]
    exclusive: int
    vendorSources: List[DestinyItemVendorSourceReference]


class DestinyObjectiveDisplayProperties(BaseModel):
    activityHash: Optional[int]
    displayOnItemPreviewScreen: bool


class DestinyItemObjectiveBlockDefinition(BaseModel):
    objectiveHashes: List[int]
    displayActivityHashes: List[int]
    requireFullObjectiveCompletion: bool
    questlineItemHash: int
    narrative: str
    objectiveVerbName: str
    queryTypeIdentifier: str
    questTypeHash: int
    perObjectiveDisplayProperties: List[DestinyObjectiveDisplayProperties]
    displayAsStatTracker: bool


class DestinyItemMetricBlockDefinition(BaseModel):
    availableMetricCategoryNodeHashes: List[int]


class DestinyItemGearsetBlockDefinition(BaseModel):
    trackingValueMax: int
    itemList: List[int]


class DestinyItemSackBlockDefinition(BaseModel):
    detailAction: str
    openAction: str
    selectItemCount: int
    vendorSackType: str
    openOnAcquire: bool


class DestinyItemSocketEntryPlugItemDefinition(BaseModel):
    plugItemHash: int


class DestinyItemSocketEntryDefinition(BaseModel):
    socketTypeHash: int
    singleInitialItemHash: int
    reusablePlugItems: List[DestinyItemSocketEntryPlugItemDefinition]
    preventInitializationOnVendorPurchase: bool
    hidePerksInItemTooltip: bool
    plugSources: int
    reusablePlugHash: Optional[int]
    randomizedPlugSetHash: Optional[int]
    defaultVisible: bool


class DestinyItemIntrinsicSocketEntryDefinition(BaseModel):
    plugItemHash: int
    socketTypeHash: int
    defaultVisible: bool


class DestinyItemSocketCategoryDefinition(BaseModel):
    socketCategoryHash: int
    socketIndexes: List[int]


class DestinyItemSocketBlockDefinition(BaseModel):
    detail: str
    socketEntries: List[DestinyItemSocketEntryDefinition]
    intrinsicSockets: List[DestinyItemIntrinsicSocketEntryDefinition]
    socketCategories: List[DestinyItemSocketCategoryDefinition]


class DestinyItemSummaryBlockDefinition(BaseModel):
    sortPriority: int


class DestinyItemTalentGridBlockDefinition(BaseModel):
    talentGridHash: int
    itemDetailString: str
    buildName: str
    hugDamageType: DamageType
    hudIcon: str


class DestinyItemInvestmentStatDefinition(BaseModel):
    statTypeHash: int
    value: int
    isConditionallyActive: bool


class DestinyItemPerkEntryDefinition(BaseModel):
    requirementDisplayString: str
    perkHash: int
    perkVisibility: ItemPerkVisibility


class DestinyInventoryItemDefinition(BaseModel):
    displayProperties: Common.DestinyDisplayPropertiesDefinition
    tooltipNotifications: List[DestinyItemTooltipNotification]
    collectibleHash: Optional[int]
    iconWatermark: str
    iconWatermarkShelved: str
    secondaryIcon: str
    secondaryOverlay: str
    secondarySpecial: str
    backgroundColor: Misc.DestinyColor
    screenshot: str
    itemTypeDisplayName: str
    flavorText: str
    uiItemDisplayStyle: str
    itemTypeAndTierDisplayName: str
    displaySource: str
    tooltipStyle: str
    action: DestinyItemActionBlockDefinition
    crafting: DestinyItemCraftingBlockDefinition
    inventory: DestinyItemInventoryBlockDefinition
    setData: DestinyItemSetBlockDefinition
    stats: DestinyItemStatBlockDefinition
    emblemObjectiveHash: Optional[int]
    equippingBlock: DestinyEquippingBlockDefinition
    translationBlock: DestinyItemTranslationBlockDefinition
    preview: DestinyItemPreviewBlockDefinition
    quality: DestinyItemQualityBlockDefinition
    value: DestinyItemValueBlockDefinition
    sourceData: DestinyItemSourceBlockDefinition
    objectives: DestinyItemObjectiveBlockDefinition
    metrics: DestinyItemMetricBlockDefinition
    plug: Items.DestinyItemPlugDefinition
    gearset: DestinyItemGearsetBlockDefinition
    sack: DestinyItemSackBlockDefinition
    sockets: DestinyItemSocketBlockDefinition
    summary: DestinyItemSummaryBlockDefinition
    talentGrid: DestinyItemTalentGridBlockDefinition
    investmentStats: List[DestinyItemInvestmentStatDefinition]
    perks: List[DestinyItemPerkEntryDefinition]
    loreHash: Optional[int]
    summaryItemHash: Optional[int]
    animations: Animations.DestinyAnimationReference
    allowActions: bool
    links: List[Links.HyperlinkReference]
    doesPostmasterPullHaveSideEffects: bool
    nonTransferrable: bool
    itemCategoryHashes: List[int]
    specialItemType: SpecialItemType
    itemType: DestinyItemType
    itemSubType: DestinyItemSubType
    classType: DestinyClass
    breakerType: DestinyBreakerType
    breakerTypeHash: Optional[int]
    equippable: bool
    damageTypeHashes: List[int]
    damageTypes: List[DamageType]
    defaultDamageType: DamageType
    defaultDamageTypeHash: Optional[int]
    seasonHash: Optional[int]
    isWrapper: bool
    traitIds: List[str]
    traitHashes: List[int]
    hash: int
    index: int
    redacted: bool


class DestinyDefinition(BaseModel):
    hash: int
    index: int
    redacted: bool

    class Config:
        extra = Extra.allow


class DestinyMaterialRequirement(BaseModel):
    itemHash: int
    deleteOnAction: bool
    count: int
    countIsConstant: bool
    omitFromRequirements: bool


class DestinyEntitySearchResultItem(BaseModel):
    hash: int
    entityType: str
    displayProperties: Common.DestinyDisplayPropertiesDefinition
    weight: float


class DestinyEntitySearchResult(BaseModel):
    suggestedWords: List[str]
    results: SearchResultOfDestinyEntitySearchResultItem


from .... import entities
from ... import Destiny
from typing import (
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from .....utils import ValidatedDatetime
from ... import Exceptions
from .. import (
    Components,
    Entities,
    DestinyGameVersions,
)

__all__ = [
    'DestinyErrorProfiles',
    'DestinyLinkedProfileResponse',
    'DestinyProfileUserInfoCard',
    'DestinyProfileResponse',
    'DestinyCharacterResponse',
    'DestinyItemResponse',
    'DestinyVendorsResponse',
    'PersonalDestinyVendorSaleItemSetComponent',
    'DestinyVendorResponse',
    'DestinyPublicVendorsResponse',
    'PublicDestinyVendorSaleItemSetComponent',
    'DestinyCollectibleNodeDetailResponse',
    'DestinyItemChangeResponse',
]

BungieMembershipType = ForwardRef('entities.BungieMembershipType')
UserInfoCard = ForwardRef('User.UserInfoCard')
DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent'
)
SingleComponentResponseOfDestinyVendorReceiptsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyVendorReceiptsComponent'
)
SingleComponentResponseOfDestinyInventoryComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyInventoryComponent'
)
SingleComponentResponseOfDestinyProfileComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyProfileComponent'
)
SingleComponentResponseOfDestinyPlatformSilverComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyPlatformSilverComponent'
)
SingleComponentResponseOfDestinyKiosksComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyKiosksComponent'
)
DictionaryComponentResponseOfint64AndDestinyKiosksComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyKiosksComponent'
)
SingleComponentResponseOfDestinyPlugSetsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyPlugSetsComponent'
)
SingleComponentResponseOfDestinyProfileProgressionComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyProfileProgressionComponent'
)
SingleComponentResponseOfDestinyPresentationNodesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyPresentationNodesComponent'
)
SingleComponentResponseOfDestinyProfileRecordsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyProfileRecordsComponent'
)
SingleComponentResponseOfDestinyProfileCollectiblesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyProfileCollectiblesComponent'
)
SingleComponentResponseOfDestinyProfileTransitoryComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyProfileTransitoryComponent'
)
SingleComponentResponseOfDestinyMetricsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyMetricsComponent'
)
SingleComponentResponseOfDestinyStringVariablesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyStringVariablesComponent'
)
DictionaryComponentResponseOfint64AndDestinyCharacterComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCharacterComponent'
)
DictionaryComponentResponseOfint64AndDestinyInventoryComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyInventoryComponent'
)
DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent'
)
DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent'
)
DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent'
)
DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent'
)
DestinyBaseItemComponentSetOfuint32 = ForwardRef('entities.DestinyBaseItemComponentSetOfuint32')
DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent'
)
DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent'
)
DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent'
)
DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent'
)
DictionaryComponentResponseOfint64AndDestinyCraftablesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint64AndDestinyCraftablesComponent'
)
DestinyItemComponentSetOfint64 = ForwardRef('entities.DestinyItemComponentSetOfint64')
SingleComponentResponseOfDestinyCharacterComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCharacterComponent'
)
SingleComponentResponseOfDestinyCharacterProgressionComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCharacterProgressionComponent'
)
SingleComponentResponseOfDestinyCharacterRenderComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCharacterRenderComponent'
)
SingleComponentResponseOfDestinyCharacterActivitiesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCharacterActivitiesComponent'
)
SingleComponentResponseOfDestinyCharacterRecordsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCharacterRecordsComponent'
)
SingleComponentResponseOfDestinyCollectiblesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCollectiblesComponent'
)
SingleComponentResponseOfDestinyCurrenciesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyCurrenciesComponent'
)
SingleComponentResponseOfDestinyItemComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemComponent'
)
SingleComponentResponseOfDestinyItemInstanceComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemInstanceComponent'
)
SingleComponentResponseOfDestinyItemObjectivesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemObjectivesComponent'
)
SingleComponentResponseOfDestinyItemPerksComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemPerksComponent'
)
SingleComponentResponseOfDestinyItemRenderComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemRenderComponent'
)
SingleComponentResponseOfDestinyItemStatsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemStatsComponent'
)
SingleComponentResponseOfDestinyItemTalentGridComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemTalentGridComponent'
)
SingleComponentResponseOfDestinyItemSocketsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemSocketsComponent'
)
SingleComponentResponseOfDestinyItemReusablePlugsComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemReusablePlugsComponent'
)
SingleComponentResponseOfDestinyItemPlugObjectivesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyItemPlugObjectivesComponent'
)
SingleComponentResponseOfDestinyVendorGroupComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyVendorGroupComponent'
)
DictionaryComponentResponseOfuint32AndDestinyVendorComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfuint32AndDestinyVendorComponent'
)
DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent'
)
DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent'
)
DestinyItemComponentSetOfint32 = ForwardRef('entities.DestinyItemComponentSetOfint32')
SingleComponentResponseOfDestinyVendorComponent = ForwardRef('entities.SingleComponentResponseOfDestinyVendorComponent')
SingleComponentResponseOfDestinyVendorCategoriesComponent = ForwardRef(
    'entities.SingleComponentResponseOfDestinyVendorCategoriesComponent'
)
DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent'
)
DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent'
)
DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent = ForwardRef(
    'entities.DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent'
)
DestinyItemComponentSetOfuint32 = ForwardRef('entities.DestinyItemComponentSetOfuint32')


class DestinyProfileUserInfoCard(BaseModel):
    dateLastPlayed: ValidatedDatetime
    isOverridden: bool
    isCrossSavePrimary: bool
    platformSilver: Optional[Components.Inventory.DestinyPlatformSilverComponent]
    unpairedGameVersions: Optional[DestinyGameVersions]
    supplementalDisplayName: Optional[str]
    iconPath: Optional[str]
    crossSaveOverride: BungieMembershipType
    applicableMembershipTypes: List[BungieMembershipType]
    isPublic: bool
    membershipType: BungieMembershipType
    membershipId: int
    displayName: str
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[int]


class DestinyErrorProfiles(BaseModel):
    errorCode: Exceptions.PlatformErrorCodes
    infoCard: UserInfoCard


class DestinyLinkedProfileResponse(BaseModel):
    profiles: List[DestinyProfileUserInfoCard]
    bnetMembership: UserInfoCard
    profilesWithErrors: List[DestinyErrorProfiles]


class DestinyProfileResponse(BaseModel):
    vendorReceipts: Optional[SingleComponentResponseOfDestinyVendorReceiptsComponent]
    profileInventory: Optional[SingleComponentResponseOfDestinyInventoryComponent]
    profileCurrencies: Optional[SingleComponentResponseOfDestinyInventoryComponent]
    profile: Optional[SingleComponentResponseOfDestinyProfileComponent]
    platformSilver: Optional[SingleComponentResponseOfDestinyPlatformSilverComponent]
    profileKiosks: Optional[SingleComponentResponseOfDestinyKiosksComponent]
    profilePlugSets: Optional[SingleComponentResponseOfDestinyPlugSetsComponent]
    profileProgression: Optional[SingleComponentResponseOfDestinyProfileProgressionComponent]
    profilePresentationNodes: Optional[SingleComponentResponseOfDestinyPresentationNodesComponent]
    profileRecords: Optional[SingleComponentResponseOfDestinyProfileRecordsComponent]
    profileCollectibles: Optional[SingleComponentResponseOfDestinyProfileCollectiblesComponent]
    profileTransitoryData: Optional[SingleComponentResponseOfDestinyProfileTransitoryComponent]
    metrics: Optional[SingleComponentResponseOfDestinyMetricsComponent]
    profileStringVariables: Optional[SingleComponentResponseOfDestinyStringVariablesComponent]
    characters: Optional[DictionaryComponentResponseOfint64AndDestinyCharacterComponent]
    characterInventories: Optional[DictionaryComponentResponseOfint64AndDestinyInventoryComponent]
    characterProgressions: Optional[DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent]
    characterRenderData: Optional[DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent]
    characterActivities: Optional[DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent]
    characterEquipment: Optional[DictionaryComponentResponseOfint64AndDestinyInventoryComponent]
    characterKiosks: Optional[DictionaryComponentResponseOfint64AndDestinyKiosksComponent]
    characterPlugSets: Optional[DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent]
    characterUninstancedItemComponents: Optional[Mapping[int, DestinyBaseItemComponentSetOfuint32]]
    characterPresentationNodes: Optional[DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent]
    characterRecords: Optional[DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent]
    characterCollectibles: Optional[DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent]
    characterStringVariables: Optional[DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent]
    characterCraftables: Optional[DictionaryComponentResponseOfint64AndDestinyCraftablesComponent]
    itemComponents: Optional[DestinyItemComponentSetOfint64]
    characterCurrencyLookups: Optional[DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent]


class DestinyCharacterResponse(BaseModel):
    inventory: Optional[SingleComponentResponseOfDestinyInventoryComponent]
    character: Optional[SingleComponentResponseOfDestinyCharacterComponent]
    progressions: Optional[SingleComponentResponseOfDestinyCharacterProgressionComponent]
    renderData: Optional[SingleComponentResponseOfDestinyCharacterRenderComponent]
    activities: Optional[SingleComponentResponseOfDestinyCharacterActivitiesComponent]
    equipment: Optional[SingleComponentResponseOfDestinyInventoryComponent]
    kiosks: Optional[SingleComponentResponseOfDestinyKiosksComponent]
    plugSets: Optional[SingleComponentResponseOfDestinyPlugSetsComponent]
    presentationNodes: Optional[SingleComponentResponseOfDestinyPresentationNodesComponent]
    records: Optional[SingleComponentResponseOfDestinyCharacterRecordsComponent]
    collectibles: Optional[SingleComponentResponseOfDestinyCollectiblesComponent]
    itemComponents: Optional[DestinyItemComponentSetOfint64]
    uninstancedItemComponents: Optional[DestinyBaseItemComponentSetOfuint32]
    currencyLookups: Optional[SingleComponentResponseOfDestinyCurrenciesComponent]


class DestinyItemResponse(BaseModel):
    characterId: Optional[int]
    item: Optional[SingleComponentResponseOfDestinyItemComponent]
    instance: Optional[SingleComponentResponseOfDestinyItemInstanceComponent]
    objectives: Optional[SingleComponentResponseOfDestinyItemObjectivesComponent]
    perks: Optional[SingleComponentResponseOfDestinyItemPerksComponent]
    renderData: Optional[SingleComponentResponseOfDestinyItemRenderComponent]
    stats: Optional[SingleComponentResponseOfDestinyItemStatsComponent]
    talentGrid: Optional[SingleComponentResponseOfDestinyItemTalentGridComponent]
    sockets: Optional[SingleComponentResponseOfDestinyItemSocketsComponent]
    reusablePlugs: Optional[SingleComponentResponseOfDestinyItemReusablePlugsComponent]
    plugObjectives: Optional[SingleComponentResponseOfDestinyItemPlugObjectivesComponent]


class DestinyVendorsResponse(BaseModel):
    vendorGroups: Optional[SingleComponentResponseOfDestinyVendorGroupComponent]
    vendors: Optional[DictionaryComponentResponseOfuint32AndDestinyVendorComponent]
    categories: Optional[DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent]
    sales: Optional[DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent]
    itemComponents: Optional[Mapping[int, DestinyItemComponentSetOfint32]]
    currencyLookups: Optional[SingleComponentResponseOfDestinyCurrenciesComponent]
    stringVariables: Optional[SingleComponentResponseOfDestinyStringVariablesComponent]


class PersonalDestinyVendorSaleItemSetComponent(BaseModel):
    saleItems: Mapping[int, Entities.Vendors.DestinyVendorSaleItemComponent]


class DestinyVendorResponse(BaseModel):
    vendor: Optional[SingleComponentResponseOfDestinyVendorComponent]
    categories: Optional[SingleComponentResponseOfDestinyVendorCategoriesComponent]
    sales: Optional[DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent]
    itemComponents: Optional[DestinyItemComponentSetOfint32]
    currencyLookups: Optional[SingleComponentResponseOfDestinyCurrenciesComponent]
    stringVariables: Optional[SingleComponentResponseOfDestinyStringVariablesComponent]


class DestinyPublicVendorsResponse(BaseModel):
    vendorGroups: Optional[SingleComponentResponseOfDestinyVendorGroupComponent]
    vendors: Optional[DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent]
    categories: Optional[DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent]
    sales: Optional[DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent]
    stringVariables: Optional[SingleComponentResponseOfDestinyStringVariablesComponent]


class PublicDestinyVendorSaleItemSetComponent(BaseModel):
    saleItems: Mapping[int, Components.Vendors.DestinyPublicVendorSaleItemComponent]


class DestinyCollectibleNodeDetailResponse(BaseModel):
    collectibles: Optional[SingleComponentResponseOfDestinyCollectiblesComponent]
    collectibleItemComponents: DestinyItemComponentSetOfuint32


class DestinyItemChangeResponse(BaseModel):
    item: DestinyItemResponse
    addedInventoryItems: List[Entities.Items.DestinyItemComponent]
    removedInventoryItems: List[Entities.Items.DestinyItemComponent]


from .... import entities
from ... import User

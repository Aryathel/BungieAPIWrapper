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
    DestinyGameVersions,
)

__all__ = [
    'DestinyErrorProfiles',
    'DestinyLinkedProfileResponse',
    'DestinyProfileUserInfoCard',
    'DestinyProfileResponse',
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
DestinyBaseItemComponentSetOfuint32 = ForwardRef(
    'entities.DestinyBaseItemComponentSetOfuint32'
)
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
DestinyItemComponentSetOfint64 = ForwardRef(
    'entities.DestinyItemComponentSetOfint64'
)


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


from .... import entities
from ... import User

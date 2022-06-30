from typing import (
    List,
    Optional,
    Mapping
)

from arya_api_framework import BaseModel

from ...utils import ValidatedDatetime
from . import (
    Components,
    Destiny,
    Fireteam,
    GroupsV2,
    Queries,
    Trending,
)
from .enums import (
    GlobalAlertType,
    GlobalAlertLevel,
)


__all__ = [
    'DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent',
    'SingleComponentResponseOfDestinyVendorReceiptsComponent',
    'SingleComponentResponseOfDestinyInventoryComponent',
    'SingleComponentResponseOfDestinyProfileComponent',
    'SingleComponentResponseOfDestinyPlatformSilverComponent',
    'SingleComponentResponseOfDestinyKiosksComponent',
    'DictionaryComponentResponseOfint64AndDestinyKiosksComponent',
    'SingleComponentResponseOfDestinyProfileProgressionComponent',
    'SingleComponentResponseOfDestinyPresentationNodesComponent',
    'SingleComponentResponseOfDestinyPlugSetsComponent',
    'SingleComponentResponseOfDestinyProfileRecordsComponent',
    'SingleComponentResponseOfDestinyProfileCollectiblesComponent',
    'SingleComponentResponseOfDestinyProfileTransitoryComponent',
    'SingleComponentResponseOfDestinyMetricsComponent',
    'SingleComponentResponseOfDestinyStringVariablesComponent',
    'DictionaryComponentResponseOfint64AndDestinyCharacterComponent',
    'DictionaryComponentResponseOfint64AndDestinyInventoryComponent',
    'DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent',
    'DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent',
    'DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent',
    'DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent',
    'DestinyBaseItemComponentSetOfuint32',
    'DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent',
    'DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent',
    'DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent',
    'DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent',
    'DictionaryComponentResponseOfint64AndDestinyCraftablesComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemRenderComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemStatsComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent',
    'DictionaryComponentResponseOfint64AndDestinyItemPerksComponent',
    'DestinyItemComponentSetOfint64',
    'SingleComponentResponseOfDestinyCharacterComponent',
    'SingleComponentResponseOfDestinyCharacterProgressionComponent',
    'SingleComponentResponseOfDestinyCharacterRenderComponent',
    'SingleComponentResponseOfDestinyCharacterActivitiesComponent',
    'SingleComponentResponseOfDestinyCharacterRecordsComponent',
    'SingleComponentResponseOfDestinyCollectiblesComponent',
    'SingleComponentResponseOfDestinyCurrenciesComponent',
    'SingleComponentResponseOfDestinyItemComponent',
    'SingleComponentResponseOfDestinyItemInstanceComponent',
    'SingleComponentResponseOfDestinyItemObjectivesComponent',
    'SingleComponentResponseOfDestinyItemPerksComponent',
    'SingleComponentResponseOfDestinyItemRenderComponent',
    'SingleComponentResponseOfDestinyItemStatsComponent',
    'SingleComponentResponseOfDestinyItemTalentGridComponent',
    'SingleComponentResponseOfDestinyItemSocketsComponent',
    'SingleComponentResponseOfDestinyItemReusablePlugsComponent',
    'SingleComponentResponseOfDestinyItemPlugObjectivesComponent',
    'SingleComponentResponseOfDestinyVendorGroupComponent',
    'DictionaryComponentResponseOfuint32AndDestinyVendorComponent',
    'DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent',
    'DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemRenderComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemStatsComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent',
    'DictionaryComponentResponseOfint32AndDestinyItemPerksComponent',
    'DestinyItemComponentSetOfint32',
    'SingleComponentResponseOfDestinyVendorComponent',
    'SingleComponentResponseOfDestinyVendorCategoriesComponent',
    'DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent',
    'DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent',
    'DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent',
    'DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent',
    'DestinyItemComponentSetOfuint32',
    'SearchResultOfDestinyEntitySearchResultItem',
    'SearchResultOfTrendingEntry',
    'SearchResultOfFireteamSummary',
    'StreamInfo',
    'GlobalAlert',
    'SearchResultOfGroupMember',
    'SearchResultOfGroupBan',
    'SearchResultOfGroupMemberApplication',
]


class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Inventory.DestinyCurrenciesComponent]]


class SingleComponentResponseOfDestinyVendorReceiptsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Profiles.DestinyVendorReceiptsComponent]


class SingleComponentResponseOfDestinyInventoryComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Inventory.DestinyInventoryComponent]


class SingleComponentResponseOfDestinyProfileComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Profiles.DestinyProfileComponent]


class SingleComponentResponseOfDestinyPlatformSilverComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Inventory.DestinyPlatformSilverComponent]


class SingleComponentResponseOfDestinyKiosksComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Kiosks.DestinyKiosksComponent]


class DictionaryComponentResponseOfint64AndDestinyKiosksComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Kiosks.DestinyKiosksComponent]]


class SingleComponentResponseOfDestinyPlugSetsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.PlugSets.DestinyPlugSetsComponent]


class SingleComponentResponseOfDestinyProfileProgressionComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Profiles.DestinyProfileProgressionComponent]


class SingleComponentResponseOfDestinyPresentationNodesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Presentation.DestinyPresentationNodesComponent]


class SingleComponentResponseOfDestinyProfileRecordsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Records.DestinyProfileRecordsComponent]


class SingleComponentResponseOfDestinyProfileCollectiblesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Collectibles.DestinyProfileCollectiblesComponent]


class SingleComponentResponseOfDestinyProfileTransitoryComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Profiles.DestinyProfileTransitoryComponent]


class SingleComponentResponseOfDestinyMetricsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Metrics.DestinyMetricsComponent]


class SingleComponentResponseOfDestinyStringVariablesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.StringVariables.DestinyStringVariablesComponent]


class DictionaryComponentResponseOfint64AndDestinyCharacterComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Characters.DestinyCharacterComponent]]


class DictionaryComponentResponseOfint64AndDestinyInventoryComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Inventory.DestinyInventoryComponent]]


class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Characters.DestinyCharacterProgressionComponent]]


class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Characters.DestinyCharacterRenderComponent]]


class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Characters.DestinyCharacterActivitiesComponent]]


class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.PlugSets.DestinyPlugSetsComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemObjectivesComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemPerksComponent]]


class DestinyBaseItemComponentSetOfuint32(BaseModel):
    objectives: Optional[DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent]
    perks: Optional[DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent]


class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Presentation.DestinyPresentationNodesComponent]]


class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Records.DestinyCharacterRecordsComponent]]


class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Collectibles.DestinyCollectiblesComponent]]


class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.StringVariables.DestinyStringVariablesComponent]]


class DictionaryComponentResponseOfint64AndDestinyCraftablesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Craftables.DestinyCraftablesComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemInstanceComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemRenderComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemStatsComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemSocketsComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemReusablePlugsComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemPlugObjectivesComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemTalentGridComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemPlugComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemObjectivesComponent]]


class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemPerksComponent]]


class DestinyItemComponentSetOfint64(BaseModel):
    instances: DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent
    renderData: DictionaryComponentResponseOfint64AndDestinyItemRenderComponent
    stats: DictionaryComponentResponseOfint64AndDestinyItemStatsComponent
    sockets: DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent
    reusablePlugs: DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent
    plugObjectives: DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent
    talentGrids: DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent
    plugStates: DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent
    objectives: DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent
    perks: DictionaryComponentResponseOfint64AndDestinyItemPerksComponent


class SingleComponentResponseOfDestinyCharacterComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Characters.DestinyCharacterComponent]


class SingleComponentResponseOfDestinyCharacterProgressionComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Characters.DestinyCharacterProgressionComponent]


class SingleComponentResponseOfDestinyCharacterRenderComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Characters.DestinyCharacterRenderComponent]


class SingleComponentResponseOfDestinyCharacterActivitiesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Characters.DestinyCharacterActivitiesComponent]


class SingleComponentResponseOfDestinyCharacterRecordsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Records.DestinyCharacterRecordsComponent]


class SingleComponentResponseOfDestinyCollectiblesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Collectibles.DestinyCollectiblesComponent]


class SingleComponentResponseOfDestinyCurrenciesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Inventory.DestinyCurrenciesComponent]


class SingleComponentResponseOfDestinyItemComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemComponent]


class SingleComponentResponseOfDestinyItemInstanceComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemInstanceComponent]


class SingleComponentResponseOfDestinyItemObjectivesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemObjectivesComponent]


class SingleComponentResponseOfDestinyItemPerksComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemPerksComponent]


class SingleComponentResponseOfDestinyItemRenderComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemRenderComponent]


class SingleComponentResponseOfDestinyItemStatsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemStatsComponent]


class SingleComponentResponseOfDestinyItemTalentGridComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemTalentGridComponent]


class SingleComponentResponseOfDestinyItemSocketsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Items.DestinyItemSocketsComponent]


class SingleComponentResponseOfDestinyItemReusablePlugsComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Items.DestinyItemReusablePlugsComponent]


class SingleComponentResponseOfDestinyItemPlugObjectivesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Items.DestinyItemPlugObjectivesComponent]


class SingleComponentResponseOfDestinyVendorGroupComponent(Components.ComponentResponse):
    data: Optional[Destiny.Components.Vendors.DestinyVendorGroupComponent]


class DictionaryComponentResponseOfuint32AndDestinyVendorComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Vendors.DestinyVendorComponent]]


class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Vendors.DestinyVendorCategoriesComponent]]


class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Responses.PersonalDestinyVendorSaleItemSetComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemInstanceComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemRenderComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemStatsComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemSocketsComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemReusablePlugsComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemPlugObjectivesComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemTalentGridComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemObjectivesComponent]]


class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemPerksComponent]]


class DestinyItemComponentSetOfint32(BaseModel):
    instances: Optional[DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent]
    renderData: Optional[DictionaryComponentResponseOfint32AndDestinyItemRenderComponent]
    stats: Optional[DictionaryComponentResponseOfint32AndDestinyItemStatsComponent]
    sockets: Optional[DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent]
    reusablePlugs: Optional[DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent]
    plugObjectives: Optional[DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent]
    talentGrids: Optional[DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent]
    plugStates: Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent]
    objectives: Optional[DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent]
    perks: Optional[DictionaryComponentResponseOfint32AndDestinyItemPerksComponent]


class SingleComponentResponseOfDestinyVendorComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Vendors.DestinyVendorComponent]


class SingleComponentResponseOfDestinyVendorCategoriesComponent(Components.ComponentResponse):
    data: Optional[Destiny.Entities.Vendors.DestinyVendorCategoriesComponent]


class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Vendors.DestinyVendorSaleItemComponent]]


class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Vendors.DestinyPublicVendorComponent]]


class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Responses.PublicDestinyVendorSaleItemSetComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemInstanceComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemRenderComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemStatsComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemSocketsComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemReusablePlugsComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Components.Items.DestinyItemPlugObjectivesComponent]]


class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent(Components.ComponentResponse):
    data: Optional[Mapping[int, Destiny.Entities.Items.DestinyItemTalentGridComponent]]


class DestinyItemComponentSetOfuint32(BaseModel):
    instances: Optional[DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent]
    renderData: Optional[DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent]
    stats: Optional[DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent]
    sockets: Optional[DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent]
    reusablePlugs: Optional[DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent]
    plugObjectives: Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent]
    talentGrids: Optional[DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent]
    plugStates: Optional[DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent]
    objectives: Optional[DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent]
    perks: Optional[DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent]


class SearchResultOfDestinyEntitySearchResultItem(BaseModel):
    results: List[Destiny.Definitions.DestinyEntitySearchResultItem]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class SearchResultOfTrendingEntry(BaseModel):
    results: List[Trending.TrendingEntry]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class SearchResultOfFireteamSummary(BaseModel):
    results: List[Fireteam.FireteamSummary]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class StreamInfo(BaseModel):
    ChannelName: str


class GlobalAlert(BaseModel):
    AlertKey: str
    AlertHtml: str
    AlertTimestamp: ValidatedDatetime
    AlertLink: str
    AlertLevel: GlobalAlertLevel
    AlertType: GlobalAlertType
    StreamInfo: StreamInfo


class SearchResultOfGroupMember(BaseModel):
    results: List[GroupsV2.GroupMember]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class SearchResultOfGroupBan(BaseModel):
    results: List[GroupsV2.GroupBan]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class SearchResultOfGroupMemberApplication(BaseModel):
    results: List[GroupsV2.GroupMemberApplication]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool

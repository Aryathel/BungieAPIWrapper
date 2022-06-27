from typing import (
    Optional,
    Mapping
)

from arya_api_framework import BaseModel

from . import (
    Components,
    Destiny
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
    objectives: DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent
    perks: DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent


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

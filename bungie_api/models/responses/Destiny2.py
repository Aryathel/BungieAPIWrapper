from typing import (
    List,
    Mapping,
    Optional,
)

from .. import entities
from .framework import BaseResponse


__all__ = [
    'GetDestinyManifest',
    'GetDestinyEntityDefinition',
    'SearchDestinyPlayerByBungieName',
    'GetLinkedProfiles',
    'GetProfile',
    'GetCharacter',
    'GetClanWeeklyRewardState',
    'GetClanBannerSource',
    'GetItem',
    'GetVendors',
    'GetVendor',
    'GetPublicVendors',
    'GetCollectibleNodeDetails',
    'TransferItem',
    'PullFromPostmaster',
    'EquipItem',
    'EquipItems',
    'SetItemLockState',
    'SetQuestTrackedState',
    'InsertSocketPlug',
    'GetPostGameCarnageReport',
    'ReportOffensivePostGameCarnageReportPlayer',
    'GetHistoricalStatsDefinition',
    'GetClanLeaderboards',
    'GetClanAggregateStats',
    'SearchDestinyEntities',
    'GetHistoricalStats',
    'GetHistoricalStatsForAccount',
    'GetActivityHistory',
    'GetUniqueWeaponHistory',
    'GetDestinyAggregateActivityStats',
    'GetPublicMilestoneContent',
    'GetPublicMilestones',
    'AwaInitializeRequest',
    'AwaProvideAuthorizationResult',
    'AwaGetActionToken',
]


class GetDestinyManifest(BaseResponse):
    Response: entities.Destiny.Config.DestinyManifest


class GetDestinyEntityDefinition(BaseResponse):
    Response: entities.Destiny.Definitions.DestinyDefinition


class SearchDestinyPlayerByBungieName(BaseResponse):
    Response: List[entities.User.UserInfoCard]


class GetLinkedProfiles(BaseResponse):
    Response: entities.Destiny.Responses.DestinyLinkedProfileResponse


class GetProfile(BaseResponse):
    Response: entities.Destiny.Responses.DestinyProfileResponse


class GetCharacter(BaseResponse):
    Response: entities.Destiny.Responses.DestinyCharacterResponse


class GetClanWeeklyRewardState(BaseResponse):
    Response: entities.Destiny.Milestones.DestinyMilestone


class GetClanBannerSource(BaseResponse):
    Response: entities.Config.ClanBanner.ClanBannerSource


class GetItem(BaseResponse):
    Response: entities.Destiny.Responses.DestinyItemResponse


class GetVendors(BaseResponse):
    Response: entities.Destiny.Responses.DestinyVendorsResponse


class GetVendor(BaseResponse):
    Response: entities.Destiny.Responses.DestinyVendorResponse


class GetPublicVendors(BaseResponse):
    Response: entities.Destiny.Responses.DestinyPublicVendorsResponse


class GetCollectibleNodeDetails(BaseResponse):
    Response: entities.Destiny.Responses.DestinyCollectibleNodeDetailResponse


class TransferItem(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class PullFromPostmaster(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class EquipItem(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class EquipItems(BaseResponse):
    Response: entities.Destiny.DestinyEquipItemResults


class SetItemLockState(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class SetQuestTrackedState(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class InsertSocketPlug(BaseResponse):
    Response: entities.Destiny.Responses.DestinyItemChangeResponse


class InsertSocketPlugFree(BaseResponse):
    Response: entities.Destiny.Responses.DestinyItemChangeResponse


class GetPostGameCarnageReport(BaseResponse):
    Response: entities.Destiny.HistoricalStats.DestinyPostGameCarnageReportData


class ReportOffensivePostGameCarnageReportPlayer(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class GetHistoricalStatsDefinition(BaseResponse):
    Response: Mapping[str, entities.Destiny.HistoricalStats.Definitions.DestinyHistoricalStatsDefinition]


class GetClanLeaderboards(BaseResponse):
    Response: Mapping[str, Mapping[str, entities.Destiny.HistoricalStats.DestinyLeaderboard]]


class GetClanAggregateStats(BaseResponse):
    Response: List[entities.Destiny.HistoricalStats.DestinyClanAggregateStat]


class SearchDestinyEntities(BaseResponse):
    Response: entities.Destiny.Definitions.DestinyEntitySearchResult


class GetHistoricalStats(BaseResponse):
    Response: Mapping[str, entities.Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod]


class GetHistoricalStatsForAccount(BaseResponse):
    Response: entities.Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult


class GetActivityHistory(BaseResponse):
    Response: entities.Destiny.HistoricalStats.DestinyActivityHistoryResults


class GetUniqueWeaponHistory(BaseResponse):
    Response: entities.Destiny.HistoricalStats.DestinyHistoricalWeaponStatsData


class GetDestinyAggregateActivityStats(BaseResponse):
    Response: entities.Destiny.HistoricalStats.DestinyAggregateActivityResults


class GetPublicMilestoneContent(BaseResponse):
    Response: Optional[entities.Destiny.Milestones.DestinyMilestoneContent]


class GetPublicMilestones(BaseResponse):
    Response: Mapping[int, entities.Destiny.Milestones.DestinyPublicMilestone]


class AwaInitializeRequest(BaseResponse):
    Response: entities.Destiny.Advanced.AwaInitializeResponse


class AwaProvideAuthorizationResult(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class AwaGetActionToken(BaseResponse):
    Response: entities.Destiny.Advanced.AwaAuthorizationResult

from typing import (
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..models import (
    queries,
    responses,
)
from ..models.entities import Fireteam as FTeam
from ..models.entities.Applications import ApplicationScopes


__all__ = [
    'Fireteam'
]


DateRangeType = Union[int, str, FTeam.FireteamDateRange]
PlatformType = Union[int, str, FTeam.FireteamPlatform]
SearchType = Union[int, str, FTeam.FireteamPublicSearchOption]
SlotType = Union[int, str, FTeam.FireteamSlotSearch]


@destinyclient
@apiclient
class Fireteam(SubClient, name='fireteam', relative_path='/Fireteam/'):
    @endpoint(
        path='/Fireteam/Clan/{groupId}/ActiveCount/',
        name='Fireteam.GetActivePrivateClanFireteamCount',
        description=(
                'Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Fireteam-GetActivePrivateClanFireteamCount.html'
            '#operation_get_Fireteam-GetActivePrivateClanFireteamCount'
        ),
        method='GET'
    )
    def get_active_private_clan_fireteam_count(
            self,
            clan_id: int
    ) -> responses.Fireteam.GetActivePrivateClanFireteamCount:
        return self.get(
            f'/Clan/{clan_id}/ActiveCount/',
            response_format=responses.Fireteam.GetActivePrivateClanFireteamCount
        )

    @endpoint(
        path=(
                '/Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}'
                '/{page}/'
        ),
        name='Fireteam.GetAvailableClanFireteams',
        description=(
            'Gets a listing of all of this clan\'s fireteams that are have available slots. Caller is not checked for '
            'join criteria so caching is maximized.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Fireteam-GetAvailableClanFireteams.html'
            '#operation_get_Fireteam-GetAvailableClanFireteams'
        ),
        method='GET'
    )
    def get_available_clan_fireteams(
            self,
            clan_id: int,
            activity_type: Optional[int] = 0,
            date_range: DateRangeType = FTeam.FireteamDateRange.All,
            platform: PlatformType = FTeam.FireteamPlatform.Any,
            slot: SlotType = FTeam.FireteamSlotSearch.NoSlotRestrictions,
            public_only: Optional[bool] = False,
            page: Optional[int] = 0,
            lang_filter: Optional[str] = None,
    ) -> responses.Fireteam.GetAvailableClanFireteams:
        date_range = FTeam.FireteamDateRange.int_validator(date_range)
        platform = FTeam.FireteamPlatform.int_validator(platform)
        slot = FTeam.FireteamSlotSearch.int_validator(slot)

        return self.get(
            f'/Clan/{clan_id}/Available/{platform}/{activity_type}/{date_range}/{slot}/{int(public_only)}/{page}/',
            parameters=queries.Fireteam.GetAvailableClanFireteams(langFilter=lang_filter),
            response_format=responses.Fireteam.GetAvailableClanFireteams
        )

    @endpoint(
        path='/Fireteam/Search/Available/{platform}/{actvityType}/{dateRange}/{slotFilter}/{page}/',
        name='Fireteam.SearchPublicAvailableClanFireteams',
        description=(
            'Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join '
            'criteria so caching is maximized.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Fireteam-SearchPublicAvailableClanFireteams.html'
            '#operation_get_Fireteam-SearchPublicAvailableClanFireteams'
        ),
        method='GET'
    )
    def search_public_available_clan_fireteams(
            self,
            platform: PlatformType = FTeam.FireteamPlatform.Any,
            activity_type: Optional[int] = 0,
            date_range: DateRangeType = FTeam.FireteamDateRange.All,
            slot: SlotType = FTeam.FireteamSlotSearch.NoSlotRestrictions,
            page: Optional[int] = 0,
            lang_filter: Optional[str] = None
    ) -> responses.Fireteam.SearchPublicAvailableClanFireteams:
        platform = FTeam.FireteamPlatform.int_validator(platform)
        date_range = FTeam.FireteamDateRange.int_validator(date_range)
        slot = FTeam.FireteamSlotSearch.int_validator(slot)

        return self.get(
            f'/Search/Available/{platform}/{activity_type}/{date_range}/{slot}/{page}/',
            parameters=queries.Fireteam.SearchPublicAvailableClanFireteams(langFilter=lang_filter),
            response_format=responses.Fireteam.SearchPublicAvailableClanFireteams
        )

    @oauth_required(ApplicationScopes.ReadGroups)
    @endpoint(
        path='/Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/',
        name='Fireteam.GetMyClanFireteams',
        description='Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Fireteam-GetMyClanFireteams.html'
            '#operation_get_Fireteam-GetMyClanFireteams'
        ),
        method='GET'
    )
    def get_my_clan_fireteams(
            self,
            clan_id: int,
            platform: PlatformType = FTeam.FireteamPlatform.Any,
            include_closed: Optional[bool] = False,
            page: Optional[int] = 0,
            lang_filter: Optional[str] = None,
            group_filter: Optional[bool] = True
    ) -> responses.Fireteam.GetMyClanFireteams:
        platform = FTeam.FireteamPlatform.int_validator(platform)

        return self.get(
            f'/Clan/{clan_id}/My/{platform}/{int(include_closed)}/{page}/',
            parameters=queries.Fireteam.GetMyClanFireteams(
                groupFilter=group_filter,
                langFilter=lang_filter
            ),
            response_format=responses.Fireteam.GetMyClanFireteams
        )

    @oauth_required(ApplicationScopes.ReadGroups)
    @endpoint(
        path='/Fireteam/Clan/{groupId}/Summary/{fireteamId}/',
        name='Fireteam.GetClanFireteam',
        description='Gets a specific fireteam.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Fireteam-GetClanFireteam.html'
            '#operation_get_Fireteam-GetClanFireteam'
        ),
        method='GET'
    )
    def get_clan_fireteam(self, clan_id: int, fireteam_id: int) -> responses.Fireteam.GetClanFireteam:
        return self.get(
            f'/Clan/{clan_id}/Summary/{fireteam_id}/',
            response_format=responses.Fireteam.GetClanFireteam
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Fireteam())

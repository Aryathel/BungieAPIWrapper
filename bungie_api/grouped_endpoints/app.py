from datetime import datetime
from typing import (
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint, validate_type

from ..models.entities.Applications import ApplicationScopes
from ..models import responses, queries
from ..decorators import oauth_required, destinyclient


@destinyclient
@apiclient
class App(SubClient, name='app', relative_path='/App'):
    @oauth_required(ApplicationScopes.ReadUserData)
    @endpoint(
        path='/App/ApiUsage/{applicationId}',
        name='App.GetApplicationApiUsage',
        href='https://bungie-net.github.io/multi/operation_get_App-GetApplicationApiUsage.html#operation_get_App-GetApplicationApiUsage',
        method='GET'
    )
    def get_application_api_usage(
            self,
            id: Optional[int] = None,
            *,
            end: Optional[datetime] = None,
            start: Optional[datetime] = None
    ) -> responses.App.GetApplicationApiUsage:
        if not id:
            id = self.root.client_id

        validate_type(id, int)
        q = queries.App.GetApplicationApiUsage(end=end, start=start)

        return self.get(f'/ApiUsage/{id}', parameters=q, response_format=responses.App.GetApplicationApiUsage)

    @endpoint(
        path='/App/FirstParty/',
        name='App.GetBungieApplications',
        href='https://bungie-net.github.io/multi/operation_get_App-GetBungieApplications.html#operation_get_App-GetBungieApplications',
        method='GET'
    )
    def get_bungie_applications(self) -> responses.App.GetBungieApplications:
        return self.get('/FirstParty/', response_format=responses.App.GetBungieApplications)


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(App())

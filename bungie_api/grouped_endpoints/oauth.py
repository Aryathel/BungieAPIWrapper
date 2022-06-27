from typing import Union
import webbrowser

from arya_api_framework import SyncClient, AsyncClient, SubClient
from yarl import URL

from ..models import responses


class OAuth(SubClient, name='oauth', relative_path='/App/OAuth/'):
    @property
    def oauth_url(self) -> str:
        return str(URL(self.root.oauth_url).with_query(client_id=self.root.client_id, response_type='code'))

    def user_auth_local(self):
        webbrowser.open(self.oauth_url)
        code = input('Please enter the API code in the response:\n')
        self.get_token(code)

    def get_token(self, code: str):
        res: responses.OAuth.Token = self.post(
            '/Token/',
            data={
                'client_id': self.root.client_id,
                'grant_type': 'authorization_code',
                'code': code
            },
            response_format=responses.OAuth.Token
        )
        self.root.bearer_token = res.access_token


def setup(client: Union[SyncClient, AsyncClient]):
    client.add_subclient(OAuth())

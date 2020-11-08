
import requests

from apps.api.settings import app


def get_token() -> str:
    """
    Getting a token after authorization
    :return: Token
    """
    token = None
    try:
        response = requests.request('post', 'http://interview.agileengine.com/auth',
                                    json={"apiKey": "23567b218376f79d9415"},
                                    headers={'Content-Type': 'application/json'})
        token = response.json()['token']
    except requests.RequestException as err:
        app.logger.error(err)
    return token


def make_request(method, url_prefix, token, api_params=None) -> requests.Response:
    """
    Make request to API
    :param method: Requests method
    :param url_prefix: Prefix for build url
    :param token: Token
    :param api_params: Url params
    :return: Response
    """
    headers = {'Authorization': f'Bearer {token}', 'content-type': 'application/json'}
    url = f'http://interview.agileengine.com{url_prefix}'
    response = None
    try:
        response = requests.request(
            method, url, params=api_params, headers=headers
        )
    except requests.RequestException as err:
        app.logger.error(err)
    return response

import requests

_client_id = 'a3cf56239ce1430b8f9ff43b69867b6a'
_client_secret = 'ZsTvRQofOaROHhmfV6p4D2X27yCC2q1t'


def get_client_id() -> str:
    global _client_id
    return _client_id


def get_client_secret() -> str:
    global _client_secret
    return _client_secret


def get_token() -> str:
    token_request_url = 'https://oauth.battle.net/token'
    data = {
        'grant_type': 'client_credentials'
    }

    client_id = get_client_id()
    client_secret = get_client_secret()
    response = requests.post(token_request_url, data=data, auth=(client_id, client_secret))

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        return access_token
    else:
        print(f'Failed to get the token. Status Code: {response.status_code}')
        print(f'Response: {response}')
        return ''




import requests
import enums

base_url = 'https://us.api.blizzard.com/hearthstone/'


def get_hearthstone_metadata(token: str, category: enums.MetadataCategory = enums.MetadataCategory.NONE, locale: str = 'ko_KR'):
    metadata_request_url = base_url + 'metadata' + (f'/{category.value}' if category != enums.MetadataCategory.NONE else '')
    response = requests.get(f'{metadata_request_url}?access_token={token}&locale={locale}')
    return response.json()


def get_card_by_id(card_id: int, token: str, locale: str = 'ko_KR'):
    card_request_url = base_url + 'cards'
    response = requests.get(f'{card_request_url}/{card_id}?access_token={token}&locale={locale}')
    return response.json()


def get_all_cards(token: str, locale: str = 'ko_KR'):
    card_request_url = base_url + 'cards'
    response = requests.get(f'{card_request_url}?access_token={token}&locale={locale}')
    return response.json()


def get_all_cards_by_game_mode(token: str, game_mode: enums.GameMode = enums.GameMode.CONSTRUCTED, locale: str = 'ko_KR'):
    card_request_url = base_url + 'cards'
    response = requests.get(f'{card_request_url}?gameMode={game_mode.value}&access_token={token}&locale={locale}')
    return response.json()

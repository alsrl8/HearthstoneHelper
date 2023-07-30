import requests
import enums

base_url = 'https://us.api.blizzard.com/hearthstone/'


class CardApiParameter:
    def __init__(self, token: str, page: int = 1, page_size: int = 1, locale: str = 'ko_KR'):
        self.token = token
        self.page = page
        self.page_size = page_size
        self.locale = locale


def add_common_query_parameters(url: str, common_param: CardApiParameter):
    return f'{url}?access_token={common_param.token}&locale={common_param.locale}&page={common_param.page}&pageSize={common_param.page_size}'


def get_hearthstone_metadata(common_param: CardApiParameter, category: enums.MetadataCategory = enums.MetadataCategory.NONE):
    metadata_request_url = base_url + 'metadata' + (f'/{category.value}' if category != enums.MetadataCategory.NONE else '')
    metadata_request_url = add_common_query_parameters(metadata_request_url, common_param)
    response = requests.get(metadata_request_url)
    return response.json()


def get_card_by_id(common_param: CardApiParameter, card_id: int):
    card_request_url = base_url + f'cards/{card_id}'
    card_request_url = add_common_query_parameters(card_request_url, common_param)
    response = requests.get(card_request_url)
    return response.json()


def get_all_cards(common_param: CardApiParameter):
    card_request_url = base_url + 'cards'
    card_request_url = add_common_query_parameters(card_request_url, common_param)
    response = requests.get(card_request_url)
    return response.json()


def get_all_cards_by_game_mode(common_param: CardApiParameter, game_mode: enums.GameMode = enums.GameMode.CONSTRUCTED):
    card_request_url = base_url + 'cards'
    card_request_url = add_common_query_parameters(card_request_url, common_param)
    response = requests.get(f'{card_request_url}&gameMode={game_mode.value}')
    return response.json()

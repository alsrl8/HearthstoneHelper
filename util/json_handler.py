import json
import os


def get_default_json_file_path():
    return './data/temp.json'


def check_json_file_exists(file_path: str) -> bool:
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    else:
        return False


def save_json_file(json_data: dict, file_path: str = ''):
    if not file_path:
        file_path = get_default_json_file_path()

    if check_json_file_exists(file_path):
        print(f'Json file already exists. File path: {file_path}')
        return

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent='\t', ensure_ascii=False)


def read_json_file(file_path: str = '') -> dict | None:
    if not file_path:
        file_path = get_default_json_file_path()

    if not check_json_file_exists(file_path):
        print(f"Json file doesn't exist. File path: {file_path}")
        return None

    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

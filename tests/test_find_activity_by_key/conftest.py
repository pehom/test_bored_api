import pytest
import requests
from config import SERVICE_URL
from src.base_classes.response import Response


@pytest.fixture
def get_random_activity_by_existing_key():
    key = '1000000'
    url = f'{SERVICE_URL}?key={key}'
    resp = Response(requests.get(url))
    print(f'\n\t {url=}')
    print('\n\t response: ', resp.value.json())
    return resp.value.json()['key']

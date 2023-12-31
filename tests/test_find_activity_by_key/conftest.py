import pytest
import requests
from config import SERVICE_URL
from src.base_classes.response import Response


@pytest.fixture
def get_random_activity_by_key(key):
    url = f'{SERVICE_URL}?key={key}'
    raw_resp = requests.get(url)
    print(raw_resp.elapsed)
    resp = Response(raw_resp)
    print(f'\n\t {url=}')
    print('\t response: ', resp.value.json())
    return resp

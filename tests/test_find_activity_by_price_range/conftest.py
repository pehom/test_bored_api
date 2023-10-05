import pytest
import requests
from config import SERVICE_URL
from src.base_classes.response import Response


@pytest.fixture
def get_random_activity_by_price_range(price_range):
    url = f'{SERVICE_URL}?minprice={price_range[0]}&&maxprice={price_range[1]}'
    resp = Response(requests.get(url))
    print(f'\n\t {url=}')
    print('\t response: ', resp.value.json())
    return resp

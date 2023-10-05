import pytest
import requests
from config import SERVICE_URL
from src.base_classes.response import Response


@pytest.fixture
def get_random_activity_by_participants(participants):
    url = f'{SERVICE_URL}?participants={participants}'
    resp = Response(requests.get(url))
    print(f'\n\t {url=}')
    print('\t response: ', resp.value.json())
    return resp

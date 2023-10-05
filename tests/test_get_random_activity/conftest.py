import pytest
import requests
from config import SERVICE_URL


@pytest.fixture
def get_random_activity():
    return requests.get(SERVICE_URL)

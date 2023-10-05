import requests
from config import SERVICE_URL
from faker import Faker
from random import random
import pytest
import requests
from config import SERVICE_URL
from src.base_classes.response import Response

if __name__ == '__main__':
    url = f'{SERVICE_URL}?key='
    raw_resp = requests.get(url)
    print(raw_resp.elapsed)
    print(raw_resp.json())
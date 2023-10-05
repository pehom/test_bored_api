import pytest
from pydantic import ValidationError


@pytest.mark.parametrize('key', [
    1000000,
    1000001,
    8125168,
    9999998,
    9999999
])
def test_get_random_activity_by_valid_key(get_random_activity_by_key, key):
    try:
        get_random_activity_by_key.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_key.check_no_activity_found()


@pytest.mark.parametrize('key', [
    999999,
    10000000,
    1000001.5,
    'key123',
    "1000000'+OR+1=1--",
    '!2*/*{}',
    ' ',
    ''
])
def test_get_random_activity_by_invalid_key(get_random_activity_by_key, key):
    get_random_activity_by_key.assert_status_code([200, 404]).check_wrong_query_arguments_error()

import pytest


@pytest.mark.parametrize('key', [
    1000000,
    1000001,
    'hui',
    8125168
])
def test_get_random_activity_by_existing_key(key, get_random_activity_by_key):
    get_random_activity_by_key.assert_status_code([404]).valid()



# def test_get_random_activity_by_nonexisting_key()
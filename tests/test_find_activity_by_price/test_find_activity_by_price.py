import pytest
from pydantic import ValidationError


@pytest.mark.parametrize('price', [
    0.0,
    0.1,
    0.9,
    1.0
])
def test_find_activity_by_valid_price(get_random_activity_by_price, price):
    try:
        get_random_activity_by_price.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_price.check_no_activity_found()


@pytest.mark.parametrize('price', [
    -0.1,
    1.1,
    "0.5'+OR+1=1--",
    'NULL',
    '',
    ' '
])
def test_find_activity_by_invalid_price(get_random_activity_by_price, price):
    get_random_activity_by_price.check_wrong_query_arguments_error()

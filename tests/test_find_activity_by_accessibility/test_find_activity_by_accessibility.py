import pytest
from pydantic import ValidationError
from faker import Faker


@pytest.mark.parametrize('accessibility', [
    0.0,
    0.1,
    0.9,
    1.0
])
def test_find_activity_by_valid_accessibility(get_random_activity_by_accessibility, accessibility):
    try:
        get_random_activity_by_accessibility.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_accessibility.check_no_activity_found()


@pytest.mark.parametrize('accessibility', [
    -0.1,
    1.1,
    "0.5'+OR+1=1--",
    'NULL',
    Faker(locale='en').word(),
    '',
    ' '
])
def test_find_activity_by_invalid_accessibility(get_random_activity_by_accessibility, accessibility):
    get_random_activity_by_accessibility.check_wrong_query_arguments_error()


import pytest
from pydantic import ValidationError


@pytest.mark.parametrize('activity_type', [
    'education',
    'recreational',
    'social',
    'diy',
    'charity',
    'cooking',
    'relaxation',
    'music',
    'busywork'
])
def test_find_activity_by_valid_type(get_random_activity_by_type, activity_type):
    try:
        get_random_activity_by_type.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_type.check_no_activity_found()


@pytest.mark.parametrize('activity_type', [
    2,
    'chilling',
    "diy'+OR+1=1--",
    '!2*/*{}',
    ' ',
    ''
])
def test_find_activity_by_invalid_type(get_random_activity_by_type, activity_type):
    get_random_activity_by_type.check_wrong_query_arguments_error()

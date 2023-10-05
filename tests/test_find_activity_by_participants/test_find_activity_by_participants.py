import pytest
from pydantic import ValidationError


@pytest.mark.parametrize('participants', [
    0,
    12
])
def test_find_activity_by_valid_participants(get_random_activity_by_participants, participants):
    try:
        get_random_activity_by_participants.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_participants.check_no_activity_found()


@pytest.mark.parametrize('participants', [
    -1,
    "1'+OR+1=1--",
    '2',
    1.5,
    'word',
    '!@#$%%*(&*()',
    ''
])
def test_find_activity_by_invalid_participants(get_random_activity_by_participants, participants):
    get_random_activity_by_participants.check_wrong_query_arguments_error()


from src.json_schemes.activity import ACTIVITY_SCHEME
from src.base_classes.response import Response
from src.pydantic_schemes.activity import ActivityModel


def test_get_random_activity(get_random_activity):
    print('\n\tresponse:', get_random_activity.json())
    Response(get_random_activity).assert_status_code(200).valid(ActivityModel)



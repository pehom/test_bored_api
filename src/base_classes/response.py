# from jsonschema import validate
from src.json_schemes.activity import ACTIVITY_SCHEME
from src.enums.global_enums import GlobalErrorMessages
from src.pydantic_schemes.activity import ActivityModel


class Response:
    def __init__(self, response):
        self.value = response

    def valid(self, schema: ActivityModel):
        schema.model_validate(self.value.json())
        return self

    def assert_status_code(self, code):
        if isinstance(code, list):
            assert self.value.status_code in code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.value.status_code == code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

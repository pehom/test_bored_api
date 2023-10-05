from pydantic import BaseModel, Field
from config import WRONG_QUERY_ARGUMENTS_ERROR_MESSAGE


class WrongQueryArgumentsErrorModel(BaseModel):
    error: str = Field(pattern=WRONG_QUERY_ARGUMENTS_ERROR_MESSAGE)

from pydantic import BaseModel, Field
from config import NO_FOUND_ERROR_MESSAGE


class NoActivityFoundErrorModel(BaseModel):
    error: str = Field(pattern=NO_FOUND_ERROR_MESSAGE)



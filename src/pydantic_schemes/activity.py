from pydantic import BaseModel
from enum import Enum


class TypeValues(Enum):
    EDUCATION = 'education'
    RECREATIONAL = 'recreational'
    SOCIAL = 'social'
    DIY = 'diy'
    CHARITY = 'charity'
    COOKING = 'cooking'
    RELAXATION = 'relaxation'
    MUSIC = 'music'
    BUSYWORK = 'busywork'


class ActivityModel(BaseModel):
    activity: str
    type: TypeValues
    participants: int
    price: float
    accessibility: float
    link: str
    key: str

    # @field_validator('key')
    # def check_key_is_greater_two_mils(cls, v):
    #     if int(v) < 2000000:
    #         raise ValidationError('key value is less than 2 mils')
    #     else:
    #         return v

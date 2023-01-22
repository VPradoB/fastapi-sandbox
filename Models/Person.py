from enum import Enum

from typing import Optional

from pydantic import BaseModel, Field

class HairColor(Enum):
    white = "White"
    brown = "Brown"
    black = "Black"
    blonde = "Blonde"
    ginger = "Ginger"


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Victor"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Prado"
    )
    age: int = Field(
        ...,
        qt=0,
        le=140,
        example=28
    )
    hair_color: Optional[HairColor] = Field(default=None, example="Black")
    is_married: Optional[bool]= Field(default=False)
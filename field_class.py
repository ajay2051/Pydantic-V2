from datetime import datetime
from decimal import Decimal
from typing import List
from uuid import uuid4

from pydantic import (BaseModel, EmailStr, Field, computed_field,
                      field_validator)


class User(BaseModel):
    id: int = Field(default_factory=lambda: uuid4().hex)


user = User()
print(user)


class Name(BaseModel):
    name: str = Field(..., alias="username")


name = Name(username="hello")
print(name)
print(name.model_dump(by_alias=False))


# Field Constraints

class Information(BaseModel):
    username: str = Field(..., min_length=2, max_length=5, pattern=r"^\w+$")  # pattern does not allow number
    email: EmailStr = Field(..., )
    age: int = Field(..., gt=0, lt=120)
    height: float = Field(..., gt=0.0)
    is_active: bool = Field(True)
    balance: Decimal = Field(..., max_digits=10, decimal_places=2)
    favourite_number: List[int] = Field(..., min_items=1)


info = Information(
    username="aaa",
    email="a@email.com",
    age=45, height=5.5,
    is_active=True,
    balance=45.2,
    favourite_number=[1, 2, 3])
print(info)
print(info.model_dump_json())


# Computed Fields

class Person(BaseModel):
    name: str
    birth_year: int

    @computed_field
    def age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.birth_year

    @field_validator('birth_year')
    @classmethod
    def validate_age(cls, value: int) -> int:
        current_year = datetime.now().year
        if current_year - value < 18:
            raise ValueError("Person must be 18 years old")
        return value


person = Person(name="ajay", birth_year=2010)
print(person)
print(person.model_dump())

from typing import Any

from pydantic import BaseModel, EmailStr, model_validator


class Owner(BaseModel):
    name: str
    email: EmailStr

    @model_validator(mode='before')
    @classmethod
    def check_sensitive_data_omitted(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if 'password' in data:
                raise ValueError('Password should not be included')
            if 'card number' in data:
                raise ValueError('Card Number should not be included')
        return data

    @model_validator(mode='after')
    def name_must_contain_space(self) -> 'Owner':
        if " " not in self.name:
            raise ValueError("Name must contain space")
        return self


print(Owner(name="ajay thakur", email="hello@gmail.com"))
try:
    owner = Owner(name="ajay thakur", email="hello@gmail.com", password="125545")
    print(owner)
except ValueError as e:
    print(e)

from pydantic import BaseModel, EmailStr, field_validator


class Owner(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if " " not in v:
            raise ValueError("Name must contain space")
        return v.title()


try:
    owner = Owner(name="ajay thakur", email="hello@gmail.com")
    print(owner)
except ValueError as e:
    print(e)

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


user = User.model_validate({"id": "1", "name": "ajay"}, strict=True)
print(user)

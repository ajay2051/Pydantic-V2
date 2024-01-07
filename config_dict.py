from pydantic import BaseModel, ConfigDict, Field


class Person(BaseModel):
    model_config = ConfigDict(populate_by_name=True)  # model_config helps to pass arguments by alias or column_name

    first_name: str | None = Field(default=None, alias="firstname")
    last_name: str = Field(alias="lastName")


data = {
    'first_name': 'John', 'last_name': 'Smith'
}

p = Person(first_name="John", lastName="Smith")
print(p.model_dump())
print(p.model_validate(data))

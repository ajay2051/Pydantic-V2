from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl, PositiveInt, conlist, field_validator


class User(BaseModel):
    id: int
    name: str = "John"


user = User(id=124, name="Ajay")

print(user)
print(user.model_fields_set)
print(user.model_dump())
print(user.model_dump_json())
print(user.model_json_schema())


# Nested Models

class Food(BaseModel):
    name: str
    price: float
    ingredients: Optional[List[str]] = None


class Restaurant(BaseModel):
    name: str
    location: str
    food: List[Food]  # Food is inherited from class Food


restaurant = Restaurant(
    name="Lovely Restaurant",
    location="Nepalese",
    food=[
        {"name": "Cheese Pizza", "price": 12.99, "ingredients": ["Salt", "Sugar"]},
        {"name": "Veggie Burger", "price": 8.99}
    ]
)

print(restaurant)
print(restaurant.model_dump())


# Additional Parser
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Employee(BaseModel):
    name: str
    position: str
    email: EmailStr


class Owner(BaseModel):
    name: str
    email: EmailStr


class Restaurant(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$")
    owner: Owner
    address: Address
    employees: conlist(Employee, min_length=2)  # conlist comes with min and max length
    no_of_seats: PositiveInt
    delivery: bool
    website: HttpUrl


restaurant_instance = Restaurant(
    name="Good Restaurant",
    owner={
        "name": "Ajay",
        "email": "hello@gmail.com"
    },
    address={
        "street": "122 Street",
        "city": "Npj",
        "state": "Luabind",
        "zip_code": "46000"
    },
    employees=[
        {
            "name": "aaaaa",
            "position": "Manager",
            "email": "abc@gmail.com"
        },
        {
            "name": "aaaaabbb",
            "position": "Manager and Director",
            "email": "abcd@gmail.com"
        }
    ],
    no_of_seats=5,
    delivery=True,
    website="http://www.tastybites.com"
)
print(restaurant_instance)
print(restaurant_instance.model_dump())

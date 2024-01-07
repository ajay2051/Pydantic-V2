from pydantic import BaseModel, Field

from datetime import datetime, timezone


class Model(BaseModel):
    numbers: list[int] = []


m1 = Model()
m2 = Model()

m1.numbers.extend([1, 2, 3])
print(m1)
print(m2.numbers)


class Log(BaseModel):
    dt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    msg: str


l1 = Log(msg="Hello")
print(l1)

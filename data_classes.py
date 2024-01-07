from dataclasses import dataclass, field
from typing import List, Optional

from pydantic import Field, TypeAdapter


@dataclass
class User:
    id: int
    name: str = 'John'
    age: Optional[int] = field(default=None, metadata=dict(title="Age of user", description='do not lie', ge=18))
    height: Optional[int] = Field(None, title='Height in cm', ge=50, le=300)
    friends: List[int] = field(default_factory=lambda: [0])


print(TypeAdapter(User).json_schema())

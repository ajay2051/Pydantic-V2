from datetime import datetime, timezone

from pydantic import field_serializer, BaseModel, Field


class Model(BaseModel):
    number: float
    dt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_serializer("number")
    def serialize_float(self, value):
        return round(value, 2)

    @field_serializer("dt", when_used="json-unless-none")
    def serialize_datatime_to_json(self, value):
        return value.strftime("%Y/%-m/%-d %I:%M %p")


m = Model(number=1 / 3)
print(m.model_dump())
print(m.model_dump_json())

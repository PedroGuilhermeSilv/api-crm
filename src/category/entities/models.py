import uuid

from pydantic import BaseModel, field_validator, model_validator

from src.category.entities.exceptions import erros

LENGTH_NAME = 150


class Category(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str

    def __str__(self):
        return f"Category: id={self.id}, name={self.name}"

    @model_validator(mode="after")
    @classmethod
    def check_based_info(cls, data: dict) -> dict:
        if not data.get("id"):
            raise erros.IdIsRequired
        if not isinstance(data.get("id"), uuid.UUID):
            raise erros.IdShouldBeUUID
        if not data.get("name"):
            raise erros.NameIsRequired
        if not isinstance(data.get("name"), str):
            raise erros.NameShouldBeString
        return data

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        if len(value) > LENGTH_NAME:
            raise erros.NameShouldBeLessThan150Characters
        return value

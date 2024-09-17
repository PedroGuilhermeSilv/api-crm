import uuid

from pydantic import BaseModel, Field, field_validator, model_validator

from src.category.entities.exceptions import erros

LENGTH_NAME = 150


class Category(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str

    def __str__(self):
        return f"Category: id={self.id}, name={self.name}"

    @model_validator(mode="before")
    @classmethod
    def check_based_info(cls, data: dict) -> dict:
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

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: uuid.UUID):
        if not value:
            raise erros.IdIsRequired
        if not isinstance(value, uuid.UUID):
            raise erros.IdShouldBeUUID
        return value

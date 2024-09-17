import uuid

from pydantic import BaseModel


class CategoryOutput(BaseModel):
    id: uuid.UUID
    name: str

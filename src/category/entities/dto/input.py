import uuid

from pydantic import BaseModel


class CategoryCreateInput(BaseModel):
    name: str


class CategoryUpdateInput(BaseModel):
    name: str
    id: uuid.UUID

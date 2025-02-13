from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4


class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str
    price: int
    stock: int
    image_url: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

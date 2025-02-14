import uuid
from typing import Any

from ninja import Schema


class Error(Schema):
    message: str


class ProductCreateInput(Schema):
    name: str
    description: str
    price: float
    stock: int
    description: str


class ProductCreateOutput(Schema):
    id: uuid.UUID
    name: str
    description: str
    price: float
    stock: int
    image_url: str


response = {
    201: ProductCreateOutput,
    200: ProductCreateOutput,
    404: Error,
    409: Error,
    400: Error,
    500: Error,
    422: Error,
}

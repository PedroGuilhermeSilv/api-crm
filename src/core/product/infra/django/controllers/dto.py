import uuid

from ninja import Schema


class Error(Schema):
    message: str


class ProductCreateDto(Schema):
    name: str
    description: str
    price: float
    stock: int
    description: str
    image_url: str


class ProductOutputDto(Schema):
    id: uuid.UUID
    name: str
    description: str
    price: float
    stock: int
    image_url: str


response = {
    201: ProductOutputDto,
    200: ProductOutputDto,
    404: Error,
    409: Error,
    400: Error,
    500: Error,
    422: Error,
}

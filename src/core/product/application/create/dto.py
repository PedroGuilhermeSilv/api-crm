from pydantic import BaseModel


class CreateProductInputDto(BaseModel):
    name: str
    description: str
    price: int
    stock: int
    image_url: str


class CreateProductOutputDto(BaseModel):
    id: str
    name: str
    description: str
    price: int
    stock: int
    image_url: str

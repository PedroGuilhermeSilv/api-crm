from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str
    description: str
    price: int
    stock: int
    image_url: str


class ProductOutput(BaseModel):
    id: str
    name: str
    description: str
    price: int
    stock: int
    image_url: str

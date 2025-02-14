from pydantic import BaseModel
from src.core.product.domain.value_objects import UploadedFile


class CreateProductInputDto(BaseModel):
    name: str
    description: str
    price: int
    stock: int
    image: UploadedFile

    model_config = {"arbitrary_types_allowed": True}


class CreateProductOutputDto(BaseModel):
    id: str
    name: str
    description: str
    price: int
    stock: int
    image_url: str

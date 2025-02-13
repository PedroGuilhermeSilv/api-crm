from pydantic import BaseModel, ConfigDict
from src.core.product.domain.repository import ProductRepository
from src.core.product.application.create.dto import (
    CreateProductInputDto,
    CreateProductOutputDto,
)
from src.core.product.domain.entity import Product


class CreateProduct(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    repository: ProductRepository

    async def execute(self, input: CreateProductInputDto) -> CreateProductOutputDto:
        product = Product(**input.model_dump())
        product = await self.repository.save(product)
        return CreateProductOutputDto(**product.model_dump())

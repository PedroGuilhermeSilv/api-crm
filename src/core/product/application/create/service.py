from pydantic import BaseModel, ConfigDict
from src.core.product.domain.repository import ProductRepository
from src.core.product.application.create.dto import (
    CreateProductInputDto,
    CreateProductOutputDto,
)
from src.core.product.domain.entity import Product
from src.core.storage.domain.repository import StorageRepository


class CreateProduct(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    repository: ProductRepository
    storage: StorageRepository

    async def execute(self, input: CreateProductInputDto) -> CreateProductOutputDto:
        # Primeiro salvamos o arquivo e pegamos o path
        image_path = self.storage.save_file(input.image)

        # Criamos um dict com os dados do input, substituindo image pelo image_url
        product_data = input.model_dump()
        del product_data["image"]
        product_data["image_url"] = image_path

        # Criamos e salvamos o produto
        product = Product(**product_data)
        product = await self.repository.save(product)

        return CreateProductOutputDto(**product.model_dump())

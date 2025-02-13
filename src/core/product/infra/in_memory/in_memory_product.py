from src.core.product.domain.repository import (
    ProductRepository,
    ProductOutput,
)
from src.core.product.domain.entity import Product


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products: list[Product] = []

    async def save(self, product: Product) -> ProductOutput:
        self.products.append(product)
        return ProductOutput(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            image_url=product.image_url,
        )

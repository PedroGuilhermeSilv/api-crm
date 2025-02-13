import uuid
from collections.abc import Generator

import pytest

from src.core.product.domain.repository import ProductRepository
from src.core.product.domain.entity import Product
from src.core.product.infra.in_memory.in_memory_product import InMemoryProductRepository


@pytest.fixture(scope="function")
def repository() -> Generator[ProductRepository, None, None]:
    repo = InMemoryProductRepository()
    yield repo
    repo.products.clear()


class TestSaveProductWithRepository:
    @pytest.mark.asyncio
    async def test_save_product(self, repository: ProductRepository):
        product = Product(
            name="test",
            description="test",
            price=10,
            stock=10,
            image_url="test",
        )
        product_on_db = await repository.save(product)

        print(product_on_db)

        assert product_on_db.name == product.name
        assert product_on_db.id == str(product.id)
        assert product_on_db.description == product.description
        assert product_on_db.price == product.price
        assert product_on_db.stock == product.stock
        assert product_on_db.image_url == product.image_url

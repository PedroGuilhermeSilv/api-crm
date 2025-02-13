import pytest

from src.core.product.domain.entity import Product
from src.core.product.infra.django.repository import DjangoProductRepository


@pytest.fixture
async def repository():
    repo = DjangoProductRepository()
    await repo.model.objects.all().adelete()
    yield repo


@pytest.mark.django_db
class TestCreateUserRepository:
    @pytest.mark.asyncio
    async def test_create_product(self, repository: DjangoProductRepository):
        repo = await anext(repository)
        product = Product(
            name="test",
            description="test",
            price=10,
            stock=10,
            image_url="test",
        )

        product_on_db = await repo.save(product)

        assert product_on_db.name == product.name
        assert product_on_db.id == product.id
        assert product_on_db.description == product.description
        assert product_on_db.price == product.price
        assert product_on_db.stock == product.stock
        assert product_on_db.image_url == product.image_url

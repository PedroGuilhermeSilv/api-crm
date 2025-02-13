from src.core.product.domain.repository import ProductRepository
from src.core.product.domain.dto import ProductOutput
from src.core.product.infra.django.models import Product as ProductModel
from src.core.product.domain.entity import Product


class DjangoProductRepository(ProductRepository):
    def __init__(self):
        self.model = ProductModel

    async def save(self, product: Product) -> ProductOutput:
        try:
            product_on_db = await self.model.objects.acreate(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                stock=product.stock,
                image_url=product.image_url,
            )
        except Exception as e:
            raise e

        return ProductOutput(
            id=product_on_db.id,
            name=product_on_db.name,
            description=product_on_db.description,
            price=product_on_db.price,
            stock=product_on_db.stock,
            image_url=product_on_db.image_url,
        )

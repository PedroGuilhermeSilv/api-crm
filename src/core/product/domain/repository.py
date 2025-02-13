from abc import ABC, abstractmethod

from src.core.product.domain.dto import ProductOutput
from src.core.product.domain.entity import Product


class ProductRepository(ABC):
    @abstractmethod
    async def save(self, product: Product) -> ProductOutput:
        pass

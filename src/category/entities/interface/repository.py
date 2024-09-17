from abc import ABC, abstractmethod

from src.category.entities.models import Category


class CategoryRepository(ABC):
    @abstractmethod
    def create(self, category_input: Category) -> Category:
        pass

    @abstractmethod
    def get(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def list(self) -> list[Category]:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass

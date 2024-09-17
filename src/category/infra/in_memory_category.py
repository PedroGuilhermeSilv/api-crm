from src.category.entities.interface.repository import (
    CategoryRepository,
)
from src.category.entities.models import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categorias: list[Category] = []):
        self.categories = categorias

    def create(self, category: Category) -> Category:
        self.categories.append(category)

    def get(self, category_id: int) -> Category:
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def list(self) -> list[Category]:
        return self.categories

    def update(self, category: Category) -> Category:
        for i, category_ in enumerate(self.categories):
            if category_.id == category.id:
                self.categories[i] = category
                return category
        return None

    def delete(self, category_id: int) -> None:
        for i, category in enumerate(self.categories):
            if category.id == category_id:
                self.categories.pop(i)
                return
        return

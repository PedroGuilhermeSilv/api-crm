from src.category.entities.interface.repository import (
    CategoryCreateInput,
    CategoryOutput,
    CategoryRepository,
    CategoryUpdateInput,
)
from src.category.entities.models import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categorias: list[Category] = []):
        self.categories = categorias

    def create(self, category_input: CategoryCreateInput) -> CategoryOutput:
        category = Category(**category_input.model_dump())
        self.categories.append(category)

    def get(self, category_id: int) -> CategoryOutput:
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def list(self) -> list[CategoryOutput]:
        return self.categories

    def update(self, category: CategoryUpdateInput) -> CategoryOutput:
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

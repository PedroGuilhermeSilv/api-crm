from abc import ABC, abstractmethod

from src.category.entities.dto.input import CategoryCreateInput, CategoryUpdateInput
from src.category.entities.dto.output import CategoryOutput


class CategoryRepository(ABC):
    @abstractmethod
    def create(self, category_input: CategoryCreateInput) -> CategoryOutput:
        pass

    @abstractmethod
    def get(self, category_id: int) -> CategoryOutput:
        pass

    @abstractmethod
    def list(self) -> list[CategoryOutput]:
        pass

    @abstractmethod
    def update(self, category: CategoryUpdateInput) -> CategoryOutput:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass

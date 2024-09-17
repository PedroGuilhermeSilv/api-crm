from src.category.infra.in_memory_category import Category, InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category(self):
        category = Category(name="name")
        repository = InMemoryCategoryRepository()
        category_created = repository.create(category)
        assert category_created == category

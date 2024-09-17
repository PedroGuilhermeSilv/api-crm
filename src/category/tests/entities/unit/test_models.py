import json
import uuid

import pytest

from src.category.entities.models import Category


class TestCreateCategoy:
    def test_create_with_name_empty(self):
        with pytest.raises(Exception) as exc:
            Category(id=uuid.uuid4(), name="")
        assert str(exc.value) == "Name is required"

    def test_create_with_name_greater_than_150(self):
        with pytest.raises(Exception) as exc:
            Category(id=uuid.uuid4(), name="a" * 151)
        assert str(exc.value) == "Name should be less than 150 characters"

    def test_create_with_id_empty(self):
        category = Category(name="name")
        assert category.id is not None
        assert isinstance(category.id, uuid.UUID)

    def test_create_with_id_not_uuid(self):
        with pytest.raises(Exception) as exc:
            Category(id="id", name="name")
        assert str(exc.value) == "Id should be uuid"


class TestRepresetation:
    def test_str(self):
        common_id = uuid.uuid4()
        category = Category(id=common_id, name="name")
        assert str(category) == f"Category: id={common_id}, name=name"

    def test_json(self):
        common_id = uuid.uuid4()
        category = Category(id=common_id, name="name")
        assert json.loads(category.model_dump_json()) == {
            "id": str(common_id),
            "name": "name",
        }

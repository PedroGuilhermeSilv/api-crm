import os

import pytest
from ninja.testing import TestAsyncClient

from src.framework.urls import api

os.environ["NINJA_SKIP_REGISTRY"] = "yes"

STATUS_CODE_201 = 201
STATUS_CODE_409 = 409
STATUS_CODE_400 = 400


@pytest.fixture
def client():
    return TestAsyncClient(api)


@pytest.mark.django_db(transaction=True)
class TestControllerCreateProduct:
    @pytest.mark.asyncio
    async def test_create_product(self, client):
        body = {
            "name": "test",
            "description": "test",
            "price": 10,
            "stock": 10,
            "image_url": "test",
        }

        response = await client.post("/product/", json=body)
        assert response.json().get("name") == "test"
        assert response.status_code == STATUS_CODE_201


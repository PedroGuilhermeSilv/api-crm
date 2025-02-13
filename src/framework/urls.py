from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from src.core.security.infra.django.security.application.controller.auth import (
    router as login_router,
)
from src.core.user.infra.django.application.controllers.create_user import (
    router as create_user_router,
)
from src.core.product.infra.django.controllers.create_product import (
    router as create_product_router,
)

api = NinjaAPI(urls_namespace="api-1.0.0")

api.add_router("/user", create_user_router)
api.add_router("/auth", login_router)
api.add_router("/product", create_product_router)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

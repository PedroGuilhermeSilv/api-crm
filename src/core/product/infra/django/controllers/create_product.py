from ninja import Router


from src.core.product.application.create.service import (
    CreateProduct,
    CreateProductInputDto,
    CreateProductOutputDto,
)
from src.core.product.infra.django.repository import (
    DjangoProductRepository,
)
from src.core.product.infra.django.controllers.dto import (
    ProductCreateDto,
    response,
)

router = Router()


@router.post("/", response=response)
async def create(request, product: ProductCreateDto) -> CreateProductOutputDto:
    try:
        service = CreateProduct(repository=DjangoProductRepository())
        result = await service.execute(input=CreateProductInputDto(**product.dict()))
    except Exception as e:
        return e.status_code, {"message": str(e.msg)}
    return 201, CreateProductOutputDto(**result.model_dump())

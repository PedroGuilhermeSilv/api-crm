from ninja import Router, File, Form
from ninja.files import UploadedFile
from pydantic import ValidationError

from src.core.product.application.create.service import (
    CreateProduct,
    CreateProductInputDto,
    CreateProductOutputDto,
)
from src.core.product.infra.django.repository import (
    DjangoProductRepository,
)
from src.core.product.infra.django.controllers.dto import (
    ProductCreateOutput,
    ProductCreateInput,
    response,
)
from src.core.storage.infra.tebi_io.domain.repository import TebiIOStorageRepository
from src.core.product.domain.value_objects import UploadedFile as DomainUploadedFile


router = Router()


@router.post("/", response=response)
async def create(
    request, image: UploadedFile = File(...), product: ProductCreateInput = Form(...)
) -> CreateProductOutputDto:
    # try:
        product_dict = product.model_dump()
        product_dict["image"] = DomainUploadedFile.from_upload(image)

        service = CreateProduct(
            repository=DjangoProductRepository(), storage=TebiIOStorageRepository()
        )

        result = await service.execute(input=CreateProductInputDto(**product_dict))
        return 201, CreateProductOutputDto(**result.model_dump())
    # except ValidationError as e:
    #     return 400, {"message": str(e)}
    # except Exception as e:
    #     return 500, {"message": str(e)}

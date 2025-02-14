from src.core.storage.domain.repository import StorageRepository
from src.core.product.domain.value_objects import UploadedFile
import warnings
import urllib3


class TebiIOStorageRepository(StorageRepository):

    def save_file(self, file: UploadedFile) -> str:
        # Suprime o aviso de SSL não verificado
        warnings.filterwarnings(
            "ignore", category=urllib3.exceptions.InsecureRequestWarning
        )

        # Salva o arquivo no bucket
        self.connection().put_object(
            Bucket=self.bucket_name,
            Key=file.name,
            Body=file.content,
            ContentType=file.content_type,
            ACL="public-read",
        )

        # Retorna a URL pública do arquivo
        # O formato da URL do Tebi.io é diferente do S3 padrão
        return f"{self.endpoint_url}/{self.bucket_name}/{file.name}"

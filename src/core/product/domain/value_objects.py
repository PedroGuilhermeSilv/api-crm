from pydantic import BaseModel
from typing import Any


class UploadedFile(BaseModel):
    name: str
    content: bytes
    content_type: str

    @classmethod
    def from_upload(cls, uploaded_file: Any) -> "UploadedFile":
        """
        Cria um UploadedFile a partir de um arquivo enviado via Django Ninja
        """
        content = uploaded_file.read()
        # Importante: Retornar o ponteiro do arquivo para o início
        uploaded_file.file.seek(0)

        return cls(
            name=uploaded_file.name,
            content=content,
            content_type=uploaded_file.content_type,
        )

    model_config = {"arbitrary_types_allowed": True}

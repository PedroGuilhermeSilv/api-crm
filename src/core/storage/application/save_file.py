from pydantic import BaseModel
from src.core.storage.application.dto import SaveFileInput, SaveFileOutput
from src.core.storage.domain.repository import StorageRepository


class SaveFile(BaseModel):
    repository: StorageRepository

    def execute(self, input: SaveFileInput) -> SaveFileOutput:
        self.repository.save_file(input.file)
        return SaveFileOutput(file=input.file)

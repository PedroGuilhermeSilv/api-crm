from pydantic import BaseModel


class SaveFileInput(BaseModel):
    file: str


class SaveFileOutput(BaseModel):
    file_url: str

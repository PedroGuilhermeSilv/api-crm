from abc import ABC, abstractmethod
from pydantic import BaseModel
import boto3
import os
from botocore.config import Config


class StorageRepository(BaseModel):
    service_name: str = os.environ.get("SERVICE_NAME", "s3")
    endpoint_url: str = os.environ.get("ENDPOINT_URL")
    aws_access_key_id: str = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    bucket_name: str = os.environ.get("BUCKET_NAME")

    def connection(self):
        raise NotImplementedError

    @abstractmethod
    def save_file(self, file: str) -> str:
        raise NotImplementedError

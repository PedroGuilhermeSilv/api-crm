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

    def connection(self) -> boto3.client:
        return boto3.client(
            "s3",
            endpoint_url=self.endpoint_url.replace("https://", "http://"),
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            config=Config(s3={"addressing_style": "path"}, signature_version="s3v4"),
            use_ssl=False,
            region_name="us-east-1",
        )

    @abstractmethod
    def save_file(self, file: str) -> str:
        raise NotImplementedError

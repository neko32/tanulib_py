import boto3
from enum import Enum
from typing import List, Dict, Any, Tuple
import os
from datetime import datetime


class ACLTypes(Enum):
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"


class S3ObjectKeySize:
    """Struct which contains S3 object's key and size"""

    def __init__(self, key: str, size: int) -> None:
        self._key = key
        self._size = size

    @property
    def key(self) -> str:
        return self._key

    @property
    def size(self) -> int:
        return self._size


class S3BucketListResult:
    """Result data holder for get bucket list ops"""

    def __init__(self, resp: Dict[Any, Any]) -> None:
        self.json_data = resp

    def get_list(self) -> List[Tuple[str, datetime]]:
        result = []
        for bucket in self.json_data["Buckets"]:
            result.append((bucket["Name"], bucket["CreationDate"]))
        return result


class S3ObjectListResult:
    """Result data holder for list object ops"""

    def __init__(self, resp: Dict[Any, Any]) -> None:
        self.json_data = resp

    def list_key_and_size(self) -> List[S3ObjectKeySize]:
        """returns list of each object's key and size"""
        result = []
        for content in self.json_data["Contents"]:
            result.append(S3ObjectKeySize(content["Key"], content["Size"]))
        return result


def create_s3_client():
    """
    create S3 client.
    Only if env is local_ut, then client for localstack is returned.
    """
    session = boto3.session.Session()
    env = os.environ['ENV']

    cl = session.client(
        service_name='s3',
        endpoint_url='http://localhost:4566'
    ) if env == "local_ut" else session.client(service_name='s3')
    return (session, cl)


def create_s3_bucket(
        bucket_name: str,
        acl_type: ACLTypes,
) -> str:
    """create a S3 bucket"""
    _, cl = create_s3_client()

    return cl.create_bucket(
        ACL=acl_type.value,
        Bucket=bucket_name,
    )


def delete_s3_bucket(bucket_name: str) -> bool:
    """delete a s3 bucket"""
    try:
        _, cl = create_s3_client()
        cl.delete_bucket(Bucket=bucket_name)
        return True
    except Exception as e:
        print(f"@delete_s3_bucket:error occurred - {e}")
        return False


def put_object_to_s3_bucket(bucket_name: str,
                            acl: ACLTypes,
                            key: str,
                            data: bytes) -> str:
    """persist a data with key to the specified S3 bucket"""
    _, cl = create_s3_client()
    return cl.put_object(
        Bucket=bucket_name,
        Key=key,
        ACL=acl.value,
        Body=data
    )


def delete_object_from_s3_bucket(bucket_name: str, key: str) -> bool:
    """delete an object by the specified key in the specified bucket"""
    try:
        _, cl = create_s3_client()
        cl.delete_object(Bucket=bucket_name, Key=key)
        return True
    except Exception as e:
        print(e)
        return False


def list_buckets() -> S3BucketListResult:
    """List s3 bucket"""
    _, cl = create_s3_client()
    return S3BucketListResult(cl.list_buckets())


def list_object_in_s3_bucket(bucket_name: str) -> S3ObjectListResult:
    """List all objects in the bucket specified"""
    _, cl = create_s3_client()
    return S3ObjectListResult(cl.list_objects_v2(Bucket=bucket_name))

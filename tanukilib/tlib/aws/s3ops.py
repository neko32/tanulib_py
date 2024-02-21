import boto3
from enum import Enum, auto
from typing import List, Dict, Any, Tuple
import os
from datetime import datetime


class ACLTypes(Enum):
    private = auto()
    public_read = auto()
    public_read_write = auto()
    authenticated_read = auto()


class S3ObjectKeySize:
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

    def __init__(self, resp: Dict[Any, Any]) -> None:
        self.json_data = resp

    def get_list(self) -> List[Tuple[str, datetime]]:
        result = []
        for bucket in self.json_data["Buckets"]:
            result.append((bucket["Name"], bucket["CreationDate"]))
        return result


class S3ObjectListResult:

    def __init__(self, resp: Dict[Any, Any]) -> None:
        self.json_data = resp

    def list_key_and_size(self) -> List[S3ObjectKeySize]:
        result = []
        for content in self.json_data["Contents"]:
            result.append(S3ObjectKeySize(content["Key"], content["Size"]))
        return result


def _from_acltypes_to_str(acl: ACLTypes) -> str:
    if acl == ACLTypes.private:
        return "private"
    elif acl == ACLTypes.public_read:
        return "public-read"
    elif acl == ACLTypes.public_read_write:
        return "public-read-write"
    elif acl == ACLTypes.authenticated_read:
        return "authenticated-read"
    else:
        raise NotImplementedError()


def create_s3_client():
    session = boto3.session.Session()
    env = os.environ['ENV']

    cl = session.client(
        service_name='s3',
        endpoint_url='http://localhost:4566'
    ) if env == "local_ut" else session.client(service_name='s3')
    return (session, cl)


def create_s3_bucket(bucket_name: str,
                     acl_type: ACLTypes,
                     ) -> str:
    _, cl = create_s3_client()

    return cl.create_bucket(
        ACL=_from_acltypes_to_str(acl_type),
        Bucket=bucket_name,
    )


def delete_s3_bucket(bucket_name: str) -> bool:
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
    _, cl = create_s3_client()
    return cl.put_object(
        Bucket=bucket_name,
        Key=key,
        ACL=_from_acltypes_to_str(acl),
        Body=data
    )


def delete_object_from_s3_bucket(bucket_name: str, key: str) -> bool:
    try:
        _, cl = create_s3_client()
        cl.delete_object(Bucket=bucket_name, Key=key)
        return True
    except Exception as e:
        print(e)
        return False


def list_buckets() -> S3BucketListResult:
    _, cl = create_s3_client()
    return S3BucketListResult(cl.list_buckets())


def list_object_in_s3_bucket(bucket_name: str) -> S3ObjectListResult:
    _, cl = create_s3_client()
    return S3ObjectListResult(cl.list_objects_v2(Bucket=bucket_name))

import boto3
from enum import Enum, auto
import os

class ACLTypes(Enum):
    private = auto()
    public_read = auto()
    public_read_write = auto()
    authenticated_read = auto()

def _from_acltypes_to_str(acl:ACLTypes) -> str:
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
        service_name = 's3',
        endpoint_url = 'http://localhost:4566'
    ) if env == "local_ut" else session.client(service_name = 's3')
    return (session, cl)

def create_s3_bucket(bucket_name:str,
                    acl_type:ACLTypes,
                    ) -> str:
    _, cl = create_s3_client()

    return cl.create_bucket(
        ACL = _from_acltypes_to_str(acl_type),
        Bucket = bucket_name,
    )

def delete_s3_bucket(bucket_name:str) -> bool:
    try:
        _, cl = create_s3_client()
        cl.delete_bucket(Bucket = bucket_name)
        return True
    except Exception as e:
        print(f"error occurred - {e}")
        return False

    
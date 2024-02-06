import hashlib
from typing import Tuple

def md5_from_str(s:str) -> Tuple[bytes, str]:
    md5 = hashlib.md5()
    md5.update(s.encode())
    return (md5.digest(), md5.hexdigest())

def md5_from_bytes(b:bytes) -> Tuple[bytes, str]:
    md5 = hashlib.md5()
    md5.update(b)
    return (md5.digest(), md5.hexdigest())

# [TODO] limit by size
def md5_from_file(fpath:str) -> Tuple[bytes, str]:
    md5 = hashlib.md5()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    md5.update(bytes(buf.encode()))
    return (md5.digest(), md5.hexdigest())

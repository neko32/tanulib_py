import hashlib


def md5_from_str(s: str) -> bytes:
    md5 = hashlib.md5(s.encode())
    return md5.digest()


def md5_from_bytes(b: bytes) -> bytes:
    md5 = hashlib.md5(b)
    return md5.digest()


def sha2_256_from_str(s: str) -> bytes:
    sha2_256 = hashlib.sha256(s.encode())
    return sha2_256.digest()


def sha2_256_from_bytes(b: bytes) -> bytes:
    sha2_256 = hashlib.sha256(b)
    return sha2_256.digest()


def sha2_256_from_file(fpath: str) -> bytes:
    sha256 = hashlib.sha256()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    sha256.update(bytes(buf.encode()))
    return sha256.digest()


# [TODO] limit by size


def md5_from_file(fpath: str) -> bytes:
    md5 = hashlib.md5()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    md5.update(bytes(buf.encode()))
    return md5.digest()


def to_hex(b: bytes) -> str:
    return b.hex()

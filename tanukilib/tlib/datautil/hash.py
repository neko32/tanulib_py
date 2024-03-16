import hashlib


def md5_from_str(s: str) -> bytes:
    """Generate MD5 from an input as string"""
    md5 = hashlib.md5(s.encode())
    return md5.digest()


def md5_from_bytes(b: bytes) -> bytes:
    """Generate MD5 from an input as bytes"""
    md5 = hashlib.md5(b)
    return md5.digest()


# [TODO] limit by size

def md5_from_file(fpath: str) -> bytes:
    """Generate MD5 bytes from content of the file"""
    md5 = hashlib.md5()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    md5.update(bytes(buf.encode()))
    return md5.digest()


def sha2_256_from_str(s: str) -> bytes:
    """Generate SHA2 256 from an input as string"""
    sha2_256 = hashlib.sha256(s.encode())
    return sha2_256.digest()


def sha2_256_from_bytes(b: bytes) -> bytes:
    """Generate SHA2 256 from an input as bytes"""
    sha2_256 = hashlib.sha256(b)
    return sha2_256.digest()


# [TODO] limit by size

def sha2_256_from_file(fpath: str) -> bytes:
    """Generate SHA2 256 from an input as file"""
    sha256 = hashlib.sha256()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    sha256.update(bytes(buf.encode()))
    return sha256.digest()


def sha3_256_from_str(s: str) -> bytes:
    """Generate SHA3 256 from an input as string"""
    sha3_256 = hashlib.sha3_256(s.encode())
    return sha3_256.digest()


def sha3_256_from_bytes(b: bytes) -> bytes:
    """Generate SHA3 256 from an input as bytes"""
    sha3_256 = hashlib.sha3_256(b)
    return sha3_256.digest()


# [TODO] limit by size

def sha3_256_from_file(fpath: str) -> bytes:
    """Generate SHA3 256 from content of file"""
    sha256 = hashlib.sha3_256()
    with open(fpath, 'r') as fp:
        buf = fp.read()
    sha256.update(bytes(buf.encode()))
    return sha256.digest()


def to_hex(b: bytes) -> str:
    """Derive hex str represetation for input as bytes"""
    return b.hex()


def to_binary_str_n_bits(
        x: int,
        n: int = 32,
        with_prefix=False) -> str:
    """
    Derive binary str representation for input as int.
    Result will be 0 fill with specified length n.
    Only when with_prefix is True, 0b prefix is attached.
    """
    n = n + 2 if with_prefix else n
    fmt = f"#0{n}b" if with_prefix else f"0{n}b"
    return format(x, fmt)

import decimal
import numpy as np
import random
import string
import uuid
import re
from typing import Any


def gen_scalar_randint(n:int, min_v:int, max_v:int) -> np.ndarray[Any, int]:
    return np.random.randint(min_v, max_v + 1, size = [n])

def gen_rand_alnum_str(n:int) -> str:
    alnums = string.ascii_letters + string.digits
    siz = len(alnums)
    buf = ""
    for _ in range(n):
        buf += alnums[random.randint(0, siz - 1)]
    return buf

def is_str_alnum(s:str) -> bool:
    alnums = string.ascii_letters + string.digits
    for c in s:
        if c not in alnums:
            return False
    return True

def gen_uuidv4() -> str:
    return str(uuid.uuid4())

def is_valid_uuidv4(s: str) -> bool:
    reg = re.compile(r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$")
    found = reg.findall(s)
    return len(found) > 0

def get_uuid_version(uuid_s:str) -> int:
    idx = 14
    if len(uuid_s) < idx:
        raise Exception(f"{uuid_s} length is invalid")
    ch = uuid_s[idx]
    if not ch.isdigit():
        raise Exception(f"{uuid_s} {ch} is not valid")
    return int(ch)

def can_be_guid(s:str) -> bool:
    reg = re.compile(r"^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$")
    found = reg.findall(s)
    return len(found) > 0

def round_to_nearest_half_up(v:float, decimal_point:int) -> float:
    if decimal_point <= 0:
        raise Exception(f"invalid decimal point {decimal_point}, must be greater than 0")
    
    if decimal_point == 1:
        decimal_str = '0'
    else:
        decimal_str = '0.'
        for _ in range(1, decimal_point - 1):
            decimal_str += '0'
        decimal_str += '1'
    return float(decimal.Decimal(str(v)).quantize(decimal.Decimal(decimal_str), decimal.ROUND_HALF_UP))


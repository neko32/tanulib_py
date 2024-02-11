import uuid
import re

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

    
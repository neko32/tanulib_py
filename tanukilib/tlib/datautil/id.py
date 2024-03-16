import uuid
import re


def gen_uuidv4() -> str:
    """Generate UUID Version 4"""
    return str(uuid.uuid4())


def is_valid_uuidv4(s: str) -> bool:
    """Validate whether the given string s is valid UUID Version 4"""
    reg = re.compile(
        r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$")
    found = reg.findall(s)
    return len(found) > 0


def get_uuid_version(uuid_s: str) -> int:
    """Get UUID Version provided given string uuid_s has proper format"""
    idx = 14
    if len(uuid_s) < idx:
        raise Exception(f"{uuid_s} length is invalid")
    ch = uuid_s[idx]
    if not ch.isdigit():
        raise Exception(f"{uuid_s} {ch} is not valid")
    return int(ch)


def can_be_guid(s: str) -> bool:
    """
    Check whether the given string s can be GUID.
    Major diff between GUID and UUID is UUID has a special bit
    like version and variant fields.
    """
    reg = re.compile(
        r"^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$")
    found = reg.findall(s)
    return len(found) > 0

import string


def is_str_alnum(s: str) -> bool:
    """check if given string only consists of alnum"""
    alnums = string.ascii_letters + string.digits
    for c in s:
        if c not in alnums:
            return False
    return True


def capitalize(s: str) -> str:
    """Capitalize input string s"""
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s.upper()
    else:
        return f"{s[0].upper()}{s[1:].lower()}"


def from_snake_case_to_camel_case(s: str) -> str:
    """Convert given string s from snake ase to camel case"""
    words = s.split("_")
    buf = ""
    if len(words) == 0:
        return buf
    if words[0] == "":
        return buf
    for i in range(1, len(words)):
        buf += capitalize(words[i])
    buf = words[0][0] + words[0][1:].lower() + buf
    return buf


def from_snake_case_to_pascal_case(s: str) -> str:
    """Convert given string s from snake case to pascal case"""
    return "".join([capitalize(w) for w in s.split("_")])


def from_snake_to_chain_case(s: str) -> str:
    """Convert given string s from snake ase to chain case"""
    return s.replace('_', '-').lower()


def ROT13(s: str) -> str:
    """encode/decode str by ROT13"""
    rot_tbl = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    alpha = string.ascii_letters.swapcase()
    m = {a: b for a, b in zip(alpha, rot_tbl)}
    buf = ""
    for c in s:
        buf += m[c]
    return buf

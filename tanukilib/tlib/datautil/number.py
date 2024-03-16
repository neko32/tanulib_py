import decimal


def _quote_decimal_str(decimal_point: int) -> int:
    """A helper function to quote decimal format string used by Decimal"""
    if decimal_point <= 0:
        raise Exception(
            f"invalid decimal point {decimal_point}, must be greater than 0")

    if decimal_point == 1:
        return '0'
    else:
        decimal_str = '0.'
        for _ in range(1, decimal_point - 1):
            decimal_str += '0'
        decimal_str += '1'
        return decimal_str


def round_to_nearest_half_up(v: float, decimal_point: int) -> float:
    """
    One of rounding to the nearest number.
    - 23.5 -> 24
    - 23.4 -> 23
    - -23.5 -> -23
    - -23.6 -> -24
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_HALF_UP)
    )


def round_to_nearest_half_down(v: float, decimal_point: int) -> float:
    """
    One of rounding to the nearest number.
    - 23.5 -> 23
    - 23.6 -> 24
    - -23.5 -> -24
    - -23.4 -> -23
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_HALF_DOWN)
    )


def round_to_nearest_half_even(v: float, decimal_point: int) -> float:
    """
    One of rounding to the nearest number.
    Aka banker's rounding or convergent rounding
    - 23.5 -> 24
    - 24.5 -> 24
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_HALF_EVEN)
    )


def round_truncate(v: float, decimal_point: int) -> float:
    """
    One of directed roundings.
    aka rounding toward zero
    - 23.7 -> 23
    - -23.7 -> -23
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_DOWN)
    )


def round_floor(v: float, decimal_point: int) -> float:
    """
    One of directed roundings.
    aka rounding down
    - 23.7 -> 23
    - -23.7 -> -24
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_FLOOR)
    )


def round_ceil(v: float, decimal_point: int) -> float:
    """
    One of directed roundings.
    aka rounding up
    - 23.7 -> 24
    - -23.7 -> -23
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_CEILING)
    )


def round_up(v: float, decimal_point: int) -> float:
    """
    One of directed roundings.
    - 23.7 -> 24
    - -23.7 -> -23
    """
    decimal_str = _quote_decimal_str(decimal_point)
    return float(decimal.Decimal(str(v)).quantize(
        decimal.Decimal(decimal_str),
        decimal.ROUND_UP)
    )


def get_two_complement(n: int, n_digits: int = 32) -> str:
    """Derive two complement for input. Output will have n_digits length"""
    if n >= 0:
        raise ValueError(f"value {n} must be negative")
    return bin(((1 << n_digits) - 1) & n)


def from_binary_to_hex(bs: str) -> str:
    """
    derive hex str representation for bs.
    It assumes bs has binary str representation.
    """
    bs = bs if bs.startswith("0b") else f"0b{bs}"
    return hex(int(bs, base=2))

import decimal


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

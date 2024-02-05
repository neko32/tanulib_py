

def conv_temperature_from_celsius_to_fahrenheit(c:float) -> float:
    return 32. + ((9 * c) / 5)

def conv_temperature_from_fahrenheit_to_celsius(f:float) -> float:
    return ((f - 32) * 5) / 9

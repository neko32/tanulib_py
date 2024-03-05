
from unittest import TestCase, main
from tlib.physics.weather import *


class WeatherTest(TestCase):

    def test_temperature_conv(self):
        orig_c = 15.
        f = conv_temperature_from_celsius_to_fahrenheit(orig_c)
        c_from_f = conv_temperature_from_fahrenheit_to_celsius(f)
        self.assertEqual(f, 59.)
        self.assertEqual(orig_c, c_from_f)


if __name__ == "__main__":
    main()

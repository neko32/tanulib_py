from tlib.physics.weather import WeatherAPIProvider, WeatherRegion
import os
import pprint


def main():
    api_key = os.environ['API__WEATHER__local_ut__APIKEY']
    wp = WeatherAPIProvider()
    wp.set_apikey(api_key)
    wr = WeatherRegion(city="Tokyo")
    w_info = wp.retrieve_current_weather(wr)
    pprint.pprint(w_info)


if __name__ == "__main__":
    main()

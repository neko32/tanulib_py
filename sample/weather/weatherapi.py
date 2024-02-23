from tlib.physics.weather import WeatherAPIProvider, WeatherRegion
from tlib.core.cfg import Cfg
import os
import pprint


def main():
    cfg = Cfg('local_ut')
    api_key = cfg.get_api_conf_value('WEATHER', 'APIKEY')
    wp = WeatherAPIProvider()
    wp.set_apikey(api_key)
    wr = WeatherRegion(city="Tokyo")
    w_info = wp.retrieve_current_weather(wr)
    pprint.pprint(w_info)


if __name__ == "__main__":
    main()


from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import requests


class WeatherRegion:

    def __init__(
            self,
            city: Optional[str],
            country: Optional[str] = None,
            zip: Optional[str] = None,
            lat: Optional[int] = None,
            lon: Optional[int] = None):
        self._city = city
        self._country = country
        self._zip = zip
        self._lat = lat
        self._lon = lon

    @property
    def city(self) -> Optional[str]:
        return self._city

    @property
    def country(self) -> Optional[str]:
        return self._country

    @property
    def zip(self) -> Optional[str]:
        return self._zip

    @property
    def lat(self) -> Optional[int]:
        return self._lat

    @property
    def alt(self) -> Optional[int]:
        return self.alt


class WeatherInfoProvider(ABC):

    @abstractmethod
    def set_apikey(self, api_key: str) -> None:
        pass

    @abstractmethod
    def retrieve_current_weather(
        self,
        wr: WeatherRegion
    ) -> Optional[Dict[str, Any]]:
        pass


class WeatherAPIProvider(WeatherInfoProvider):

    def set_apikey(self, api_key: str) -> None:
        self.api_key = api_key

    def retrieve_current_weather(
            self,
            wr: WeatherRegion
    ) -> Optional[Dict[str, Any]]:

        if wr.city is None:
            raise Exception("City must be specified")

        base = "http://api.weatherapi.com/v1/current.json"
        apikey = f"key={self.api_key}"
        query_params = f"q={wr.city}"
        url = f"{base}?{apikey}&{query_params}"
        result = requests.get(url)
        if result.status_code != 200:
            return None
        else:
            return result.json()


def conv_temperature_from_celsius_to_fahrenheit(c: float) -> float:
    return 32. + ((9 * c) / 5)


def conv_temperature_from_fahrenheit_to_celsius(f: float) -> float:
    return ((f - 32) * 5) / 9

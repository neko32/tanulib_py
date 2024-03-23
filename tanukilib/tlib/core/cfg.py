
import dotenv
import os
from pathlib import Path
from typing import Optional


class Cfg:
    """
    Manages configuration.
    Config location is assumed as $TANULIB_CONF_DIR}{app_name}/$env/.env
    """

    def __init__(self, env: str, app_name: str = "tlib"):
        """
        env and appname will be used as path for the configuration
        """
        self.env = env
        cfg_path = Path(os.environ['TANULIB_CONF_DIR']).joinpath(
            app_name, f"{self.env}.env")
        if not dotenv.load_dotenv(cfg_path, verbose=True):
            raise Exception("failed to initialize config")

    def get_conf_value_as_str(self, attrib: str) -> Optional[str]:
        """get conf value as string"""
        return os.environ[attrib]

    def get_conf_value_as_int(self, attrib: str) -> Optional[int]:
        """get conf value as integer"""
        return int(os.environ[attrib])

    def get_conf_value_as_float(self, attrib: str) -> Optional[float]:
        """get conf value as float"""
        return float(os.environ[attrib])

    def get_api_conf_value(self, api: str, attrib: str) -> Optional[str]:
        """get API configuraiton value. API configuration must start with API_"""
        key = f"API_{api}_{attrib}"
        return os.environ[key]

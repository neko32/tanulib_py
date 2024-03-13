
import dotenv
import os
from pathlib import Path
from typing import Optional


class Cfg:
    def __init__(self, env: str):
        self.env = env
        cfg_path = Path(os.environ['TANULIB_CONF_DIR']).joinpath("tlib", self.env, ".env")
        if not dotenv.load_dotenv(cfg_path, verbose = True):
            raise Exception("failed to initialize config")

    def get_conf_value_as_str(self, attrib: str) -> Optional[str]:
        return os.environ[attrib]

    def get_conf_value_as_int(self, attrib: str) -> Optional[int]:
        return int(os.environ[attrib])

    def get_api_conf_value(self, api: str, attrib: str) -> Optional[str]:
        key = f"API_{api}_{attrib}"
        return os.environ[key]

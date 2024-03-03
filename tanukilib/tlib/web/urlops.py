from urllib.parse import urlparse
from typing import List, Optional, Dict


class URL:

    def __init__(self, url_str: str) -> None:
        self.raw_url = url_str
        try:
            self.parsed = urlparse(url_str)
        except Exception as e:
            print(e)
            raise e

    @property
    def scheme(self) -> str:
        return self.parsed.scheme

    def scheme_domain_port(self) -> str:
        buf = f"{self.scheme}://{self.parsed.hostname}"
        if self.parsed.port is not None:
            buf += f":{self.parsed.port}"
        return buf

    def path(self) -> Optional[List[str]]:
        paths = list(filter(lambda x: x != "", self.parsed.path.split('/')))
        if not paths:
            return None
        else:
            return paths

    def query(self) -> Optional[Dict[str, str]]:
        q = self.parsed.query
        if q == "":
            return None
        else:
            try:
                return {k: v for k, v in [a.split("=") for a in q.split("&")]}
            except ValueError:
                print("parse failure! returning empty dict..")
                return {}

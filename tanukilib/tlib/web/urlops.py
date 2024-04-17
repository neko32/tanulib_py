from urllib.parse import urlparse
from urllib.request import urlretrieve
from typing import List, Optional, Dict


class URL:
    """A Wrapper of URL to provide convenient funtions"""

    def __init__(self, url_str: str) -> None:
        self.raw_url = url_str
        try:
            self.parsed = urlparse(url_str)
        except Exception as e:
            print(e)
            raise e

    @property
    def scheme(self) -> str:
        """
        Returns parsed scheme.
        e.g. http, https
        """
        return self.parsed.scheme

    def scheme_domain_port(self) -> str:
        """
        Returns cancatenated string of parsed scheme, domain and port
        e.g. https://www.takoneko.org:3000
        """
        buf = f"{self.scheme}://{self.parsed.hostname}"
        if self.parsed.port is not None:
            buf += f":{self.parsed.port}"
        return buf

    def path(self) -> Optional[List[str]]:
        """
        Returns list of path if exists. If not, None
        e.g. http://tako.net/tako/neko -> list with "tako", "neko"
        """
        paths = list(filter(lambda x: x != "", self.parsed.path.split('/')))
        if not paths:
            return None
        else:
            return paths

    def query(self) -> Optional[Dict[str, str]]:
        """
        Returns map of each query's key and value if exists. If not None
        e.g. http://neko.net?a=1&b=2  -> map {"a":"1","b":"2"}
        """
        q = self.parsed.query
        if q == "":
            return None
        else:
            try:
                return {k: v for k, v in [a.split("=") for a in q.split("&")]}
            except ValueError:
                print("parse failure! returning empty dict..")
                return {}

    def copy(
        self,
        local_path: str
    ) -> None:
        """Copy the remote content to local_path"""
        try:
            urlretrieve(self.raw_url, local_path)
        except Exception as e:
            raise e

from urllib.parse import urlparse, urlencode
from urllib.request import urlretrieve, Request, urlopen
from typing import List, Optional, Dict, Any
import json


class URL:
    """A Wrapper of URL to provide convenient funtions"""

    def __init__(self, url_str: str, qparams: Optional[Dict[str, str]] = None) -> None:
        try:
            if qparams is not None:
                encoded_qparams = urlencode(qparams)
                if url_str.endswith('/'):
                    url_str = url_str[:-1]
                self.raw_url = f"{url_str}?{encoded_qparams}"
            else:
                self.raw_url = url_str

            self.parsed = urlparse(self.raw_url)
            self.headers = {}
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

    def domain_port(self) -> str:
        """
        Returns cancatenated string of parsed domain and port
        e.g. takoneko.org:3000
        """
        buf = f"{self.parsed.hostname}"
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

    def add_header(self, k: str, v: str) -> None:
        """Add headers used in http request"""
        self.headers[k] = v

    def get_str_response(self, encoding: str) -> str:
        """Send GET method and expect ro receive string response"""
        req = Request(self.raw_url, headers=self.headers, method='GET')
        with urlopen(req) as resp:
            return resp.read().decode(encoding)

    def get_with_json_resp(
        self,
        encoding: str = "UTF-8"
    ) -> Dict[str, Any]:
        """send GET method and expect to receive JSON response"""
        req = Request(self.raw_url, headers=self.headers, method='GET')
        with urlopen(req) as resp:
            retj = json.loads(resp.read().decode(encoding))
        return retj

    def post_with_json_resp(
        self,
        body: str,
        encoding: str = "UTF-8",
    ) -> Dict[str, Any]:
        """send POST method and expect to receive JSON response"""
        req = Request(
            self.raw_url,
            headers=self.headers,
            method='POST',
            data=bytes(body, encoding)
        )
        with urlopen(req) as resp:
            retj = json.loads(resp.read().decode(encoding))
        return retj

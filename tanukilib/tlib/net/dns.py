from enum import Enum
from typing import Optional, List
import dns.resolver


class RDataType(Enum):
    """Represent RDataType"""
    TXT = 'TXT'
    CNAME = 'CNAME'
    SOA = 'SOA'
    NAMESERVER = 'NS'
    ADDRESS = 'A'
    MAIL_EXCHANGE = 'MX'
    HINFO = 'HINFO'
    IPV6_ADDRESS = 'AAAA'


class DNSResolver:
    """DNS Resolver"""

    def __init__(self, url: str, rdata_type: RDataType):
        self.url = url
        self.rdata_type = rdata_type
        self._qname = None
        self._ans_size = None
        self._resp_cache = {}
        self._serial = None
        self._refresh = None
        self._expire = None
        self._mname = None
        self._txt = None
        self._nameservers = None
        self._addresses = None
        self._addresses_v6 = None

    @property
    def txt(self) -> Optional[str]:
        return self._txt

    @property
    def nameservers(self) -> Optional[List[str]]:
        return self._nameservers

    @property
    def addresses(self) -> Optional[List[str]]:
        return self._addresses

    @property
    def address_v6(self) -> Optional[List[str]]:
        return self._addresses_v6

    @property
    def qname(self) -> Optional[str]:
        return self._qname

    @property
    def last_answer_size(self) -> Optional[int]:
        return self._ans_size

    def query(self, verbose: bool = False) -> None:
        """Send DNS Query"""
        ans = dns.resolver.resolve(self.url, self.rdata_type.value)
        if verbose:
            print(f"qname:{ans.qname}, size:{len(ans)}")
        if self.rdata_type == RDataType.TXT:
            for rdata in ans:
                for rdata_str in rdata.strings:
                    if verbose:
                        print(rdata_str)
                    self._txt = str(rdata_str, encoding='utf-8')

        if self.rdata_type == RDataType.NAMESERVER:
            ns_list = []
            for rdata in ans:
                if verbose:
                    print(str(rdata.target))
                ns_list.append(str(rdata.target))
            self._nameservers = ns_list

        if self.rdata_type == RDataType.ADDRESS:
            addr_list = []
            for rdata in ans:
                if verbose:
                    print(str(rdata.address))
                addr_list.append(str(rdata.address))
            self._addresses = addr_list

        if self.rdata_type == RDataType.IPV6_ADDRESS:
            addr_list = []
            for rdata in ans:
                if verbose:
                    print(str(rdata.address))
                addr_list.append(str(rdata.address))
            self._addresses_v6 = addr_list

        self._qname = str(ans.qname)
        self._ans_size = len(ans)

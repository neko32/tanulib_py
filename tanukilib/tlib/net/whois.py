from tlib.core import exec_cmd
from tlib.datautil.string import split_by_multiple_spaces
from tlib.datautil.vector import discard_till
from typing import List


class WhoisInfo:
    """Parse and Persist who is result"""

    def __init__(self, whois_resp: str):
        self._tech_contact = []
        self._name_server = []
        self._parse(whois_resp)

    @property
    def domain_name(self) -> str:
        return self._domain_name

    @property
    def organization(self) -> str:
        return self._organization

    @property
    def organization_type(self) -> str:
        return self._organization_type

    @property
    def administrative_contact(self) -> str:
        return self._admin_contact

    @property
    def technical_contact(self) -> List[str]:
        return self._tech_contact

    @property
    def name_server(self) -> List[str]:
        return self._name_server

    @property
    def signing_key(self) -> str:
        return self._signing_key

    @property
    def state(self) -> str:
        return self._state

    @property
    def registered_date(self) -> str:
        return self._registered_date

    @property
    def connected_date(self) -> str:
        return self._connected_date

    @property
    def last_update(self) -> str:
        return self._last_update

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        buf = "{\n"
        buf += f"\tDomain Name:{self.domain_name},\n"
        buf += f"\tOrganization:{self.organization},\n"
        buf += f"\tOrganization Type:{self.organization_type},\n"
        buf += f"\tAdministrative Contact:{self.administrative_contact},\n"
        buf += f"\tTechnical Contact:{self.technical_contact},\n"
        buf += f"\tName Server:{self.name_server},\n"
        buf += f"\tSigning Key:{self.signing_key},\n"
        buf += f"\tState:{self.state},\n"
        buf += f"\tRegistered Date:{self.registered_date},\n"
        buf += f"\tConnected Date:{self.connected_date},\n"
        buf += f"\tLast Update:{self.last_update}\n"
        buf += "}\n"
        return buf

    def _parse(self, s: str):
        """Perform parsing who is result"""
        lines = s.splitlines()
        lines = discard_till(lines, "Domain Information:", True)
        for line in lines:
            if len(line) == 0:
                continue
            if not line.startswith("["):
                key_start_idx = line.find("[")
                if key_start_idx == -1:
                    raise ValueError(
                        "failed to process. Key bracket not found")
                line = line[key_start_idx:]
            vals = split_by_multiple_spaces(line)
            if not vals[0].endswith("]"):
                vals = [" ".join(vals[:2]), " ".join(vals[2:])]
            else:
                vals = [vals[0], " ".join(vals[1:])]
            if len(vals) != 2:
                raise ValueError(
                    "failed to process - not expected whois format")
            key = vals[0]
            val = vals[1]
            print(f"key:{key},val:{val}")
            if key == "[Domain Name]":
                self._domain_name = val
            elif key == "[Organization]":
                self._organization = val
            elif key == "[Organization Type]":
                self._organization_type = val
            elif key == "[Administrative Contact]":
                self._admin_contact = val
            elif key == "[Technical Contact]":
                self._tech_contact.append(val)
            elif key == "[Name Server]":
                self._name_server.append(val)
            elif key == "[Signing Key]":
                self._signing_key = val
            elif key == "[State]":
                self._state = val
            elif key == "[Registered Date]":
                self._registered_date = val
            elif key == "[Connected Date]":
                self._connected_date = val
            elif key == "[Last Update]":
                self._last_update = val


def whois(domain: str) -> WhoisInfo:
    """Execute whois. If not found, None is returned"""
    retcode, stdout, _ = exec_cmd(["whois", domain])
    if retcode != 0:
        return None

    return WhoisInfo(stdout)

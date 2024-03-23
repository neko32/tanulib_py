from tlib.core import exec_cmd
import re
from io import StringIO
import pandas as pd


# [TODO] biased with Ubuntu 22


class LSBInfo:
    """Stores LSB commands' result"""

    def __init__(self):
        """As a prep of the class, execute lsb_release command and persist results"""
        ret_code, stdout, _ = exec_cmd(['lsb_release', '-a'])
        if ret_code != 0:
            raise Exception("lsb_release command failed")

        for idx, line in enumerate(stdout.splitlines()):
            if not line.startswith("NO LSB"):
                if idx == 0:
                    self._distributor_id = line.split(":")[1].strip()
                if idx == 1:
                    self._description = line.split(":")[1].strip()
                if idx == 2:
                    self._release = line.split(":")[1].strip()
                if idx == 3:
                    self._codename = line.split(":")[1].strip()

    @property
    def distributor_id(self) -> str:
        return self._distributor_id

    @property
    def description(self) -> str:
        return self._description

    @property
    def release(self) -> str:
        return self._release

    @property
    def codename(self) -> str:
        return self._codename


def ss_tcp_udp_established() -> pd.DataFrame:
    """execute ss -uta and return result as pandas.DataFrame"""
    cmd = ['ss', '-uta']
    _, out, _ = exec_cmd(cmd)
    reg = re.compile(' +')
    out = reg.sub(',', out)
    reg = re.compile(',\n')
    out = reg.sub('\n', out)
    reg = re.compile(',$')
    out = reg.sub('', out)
    fs = StringIO(out)
    return pd.read_csv(fs)

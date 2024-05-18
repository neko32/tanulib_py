from tlib.core.core import exec_cmd
from pandas import DataFrame
from typing import Optional


class NVSMI:
    """A Wrapper of nvidia-smi"""

    def __init__(self):
        self._result = None

    def query(self) -> DataFrame:
        """run gpu query"""

        params = [
            "name", "pci.bus_id",
            "driver_version", "pstate", "pcie.link.gen.max",
            "pcie.link.gen.current", "temperature.gpu",
            "utilization.gpu", "utilization.memory",
            "memory.total", "memory.free", "memory.used"
        ]

        params_str = ",".join(params)
        ret_code, stdout, _ = exec_cmd(
            ['nvidia-smi', f"--query-gpu={params_str}", "--format=csv"])
        if ret_code != 0:
            raise Exception("nvidia-smi failed")
        lines = stdout.splitlines()
        headers = [s.strip() for s in lines[0].split(",")]
        print(headers)
        data = [[s.strip() for s in line.split(",")] for line in lines[1:]]
        self._result = DataFrame(
            columns=headers,
            data=data
        )
        return self._result

    def get_cached_result(self) -> Optional[DataFrame]:
        return self._result

    def persist_disk(self, fpath: str) -> None:
        """Persist result as csv to the specified file"""
        if self._result is not None:
            self._result.to_csv(fpath)

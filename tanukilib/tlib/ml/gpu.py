from tlib.core.core import exec_cmd


class GPUInfo:
    """Contains GPU info"""

    def __init__(self):
        self._name = None


class NVSMI:
    """A Wrapper of nvidia-smi"""

    def __init__(self):
        self.params = []

    def add_name(self):
        """add name to gpu query"""
        self.params.append('name')

    def query(self) -> list[GPUInfo]:
        """run gpu query"""
        params_str = ",".join(self.params)
        ret_code, stdout, _ = exec_cmd(
            ['nvidia-smi', f"--query-gpu={params_str}", "--format=csv"])
        if ret_code != 0:
            raise Exception("nvidia-smi failed")
        print(stdout)
        gpus = []
        return gpus

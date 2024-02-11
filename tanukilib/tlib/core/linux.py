from tlib.core import exec_cmd

# [TODO] biased with Ubuntu 22
class LSBInfo:
    def __init__(self):
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


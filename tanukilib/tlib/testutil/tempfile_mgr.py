import os
from pathlib import Path
from tlib.datautil import gen_rand_alnum_str

class TempFileNameManager:
    """Manages temp files for test"""

    def __init__(self):
        self.tempfile_dir = Path(os.environ["HOME_TMP_DIR"])
        if not self.tempfile_dir.exists():
            raise Exception(f"HOME_TMP_DIR env var must be set")
        self.cache = {} 

    def generate(self, key:str) -> str:
        """Generate a tempfile"""
        rt = gen_rand_alnum_str(14)
        fpath = str(self.tempfile_dir.joinpath(rt))
        self.cache[key] = fpath
        return fpath

    def remove(self, key):
        """If cache has the specified key, remove the temp file"""
        if key not in self.cache:
            raise Exception(f"{key} hasn't registered in the manager")
        fpath = Path(self.cache[key])
        fpath.unlink()
        

        
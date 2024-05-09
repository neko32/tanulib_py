from pathlib import Path
import os


def get_tmp_dir() -> str:
    """Get temp dir (HOME_TMP_DIR)"""
    path = Path(os.environ["HOME_TMP_DIR"])
    if not path.exists():
        raise Exception("HOME_TMP_DIR must be set in env variable")
    return str(path)

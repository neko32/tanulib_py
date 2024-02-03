from typing import Optional
from os import remove, rmdir, listdir

def split_filename_postfix(file_name:str) -> (str, Optional[str]):
    sp = file_name.split('.')
    if len(sp) == 1:
        return (sp[0], None)
    else:
        return (".".join(sp[0:-1]), sp[-1])

def rmdir_and_files(dir_path:str) -> (int, int):
    success_n = 0
    fail_n = 0
    for f in listdir(dir_path):
        try:
            remove(f"{dir_path}/{f}")
            success_n += 1
        except:
            fail_n += 1

    if fail_n == 0:
        rmdir(dir_path)

    return (success_n, fail_n)


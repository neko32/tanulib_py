import multiprocessing
import subprocess
from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple

def get_num_cpu() -> int:
    return multiprocessing.cpu_count()

def exec_parallel_sync(max_num, f, *inputs):
    with multiprocessing.Pool(max_num) as p:
        return p.map(f, *inputs)

def exec_parallel_async(max_num, f, *inputs):
    with ProcessPoolExecutor(max_num) as executor:
        return executor.map(f, *inputs)

def exec_cmd(params:List[str]) -> Tuple[int, str, str]:
    ps = subprocess.run(params, capture_output = True, text = True)
    stdout = ps.stdout
    stderr = ps.stderr
    ret_code = ps.returncode
    return (ret_code, stdout, stderr)

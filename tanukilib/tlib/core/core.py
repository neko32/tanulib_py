import multiprocessing
import subprocess
from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple


def get_num_cpu() -> int:
    """get num of CPU"""
    return multiprocessing.cpu_count()


def exec_parallel_sync(max_num, f, *inputs):
    """execute f with max {max_num} concurrency in sync manner"""
    with multiprocessing.Pool(max_num) as p:
        return p.map(f, *inputs)


def exec_parallel_async(max_num, f, *inputs):
    """execute f with max {max_num} concurrency in async manner"""
    with ProcessPoolExecutor(max_num) as executor:
        return executor.map(f, *inputs)


def exec_cmd(params: List[str]) -> Tuple[int, str, str]:
    """execute command"""
    ps = subprocess.run(params, capture_output=True, text=True)
    stdout = ps.stdout
    stderr = ps.stderr
    ret_code = ps.returncode
    return (ret_code, stdout, stderr)


def exec_cmd_with_pipe(
    params: List[str],
    piped_params: List[str]
) -> str:
    """execute command. The result is sent to a pipe and then piped_params are executed"""
    ps = subprocess.Popen(tuple(params), stdout=subprocess.PIPE)
    print(ps.stdout)
    stdout = subprocess.check_output(tuple(piped_params), stdin=ps.stdout)
    ps.wait()
    return stdout.decode('utf-8') if stdout is not None else ""

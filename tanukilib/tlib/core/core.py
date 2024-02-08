import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def get_num_cpu() -> int:
    return multiprocessing.cpu_count()


def exec_parallel_async(max_num, f, *inputs):
    with ProcessPoolExecutor(max_num) as executor:
        return executor.map(f, *inputs)

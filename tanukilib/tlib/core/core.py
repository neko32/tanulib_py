import multiprocessing

def get_num_cpu() -> int:
    return multiprocessing.cpu_count()

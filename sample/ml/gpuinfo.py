from tlib.ml.gpu import *


def main():
    gpu = NVSMI()
    gpu_data = gpu.query()
    cached_result = gpu.get_cached_result()
    print(gpu_data)
    print(cached_result['name'])


if __name__ == "__main__":
    main()

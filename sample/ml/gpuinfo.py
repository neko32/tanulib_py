from tlib.ml.gpu import *


def main():
    gpu = NVSMI()    
    gpu.add_name()
    gpu.query()


if __name__ == "__main__":
    main()
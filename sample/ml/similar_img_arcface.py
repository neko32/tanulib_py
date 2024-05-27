from tlib.ml.input import MNIST10Input
from tlib.ml.base import model_auto_saver
from tlib.ml.custom_layer import ArcFaceLayer

def main():

    model_name = "mnist10"
    ipt_mgr = MNIST10Input()
    ipt_mgr.process()

    



if __name__ == "__main__":
    main()
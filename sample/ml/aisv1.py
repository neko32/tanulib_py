from tlib.ml import perform_style_transfer_with_AISV1
from keras.preprocessing.image import save_img
import os
from pathlib import Path

def main():
    dataset_name = "styletransfer"
    category = "sample"
    outputs = perform_style_transfer_with_AISV1(
        dataset_name, 
        category,
        "nekocha.jpg",
        [620, 620],
        "style.jpg",
        [256, 256],
        verbose = True
    )
    print(outputs[0][0])
    print(type(outputs[0][0]).__name__)
    try:
        out_path = str(Path(os.environ["HOME_TMP_DIR"]).joinpath("style_trans.jpg"))
        save_img(out_path, outputs[0][0])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
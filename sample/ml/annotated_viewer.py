from tlib.ml.annotated import Viewer
from tlib.ml.dataset import get_data_dir
from pathlib import Path


def main():
    data_dir = str(Path(get_data_dir()).joinpath("cat_annotated", "shimax"))
    viewer = Viewer(data_dir, "catx")
    #viewer.start_as_plain_img_viewer()
    viewer.start_as_cvat_annotated_viewer()
    viewer.wait()


if __name__ == "__main__":
    main()

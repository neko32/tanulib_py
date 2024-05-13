from tlib.fileutil.imagefiles import generate_size_report
from tlib.ml.dataset import get_data_dir
from pathlib import Path


def main():
    ml_dir = str(Path(get_data_dir()).joinpath("faces_pexels", "human"))
    for k, s in generate_size_report(ml_dir).items():
        print(f"{k}: {s}")


if __name__ == "__main__":
    main()

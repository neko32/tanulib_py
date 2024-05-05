import os
from tlib.web.aozora import *
from pathlib import Path


def main():

    base_url = "https://www.aozora.gr.jp/cards"
    id = "59406_66606"
    target = f"002035/files/{id}.html"
    aozora_url = f"{base_url}/{target}"
    mldata_dir = Path(os.environ["TLIB_ML_DATA_DIR"])
    mldata_dir = mldata_dir.joinpath(
        "aozora", "novels", f"{id}_owel_facism.txt")

    out_file = str(mldata_dir)

    ao = AozoraExtractor(aozora_url)
    ao.extract(out_file)


if __name__ == "__main__":
    main()

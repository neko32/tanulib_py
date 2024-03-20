from unittest import TestCase, main
from tlib.cat.br_analysis import BloodTestReport, to_df
from tlib.fileutil import list_files_and_dirs
from pathlib import Path
from datetime import datetime
import pandas as pd
import os


class CatBTAnalysisTest(TestCase):

    def test_blood_test_import_from_antech_report(self):
        bt_antech_dir = str(Path(__file__).parent.
                            joinpath("testdata", "text", "cat_bt"))

        _, files = list_files_and_dirs(bt_antech_dir, "**/*.txt")

        tmp_dir = os.environ["HOME_TMP_DIR"]
        out_file = Path(tmp_dir).joinpath("antech_bt_result.csv")

        if out_file.exists():
            out_file.unlink()

        df = pd.DataFrame()
        dfl = []

        for bt_antech_file in files:
            if not Path(bt_antech_file).exists():
                raise Exception(
                    f"test input file not exists at {str(bt_antech_file)}")

            with open(str(bt_antech_file), "r") as fd:
                bt_report = fd.read()
            path = Path(bt_antech_file)
            print(f"processing {path.name}.. ")
            date_s = path.name.split("_")[0]
            rep_name = path.name.split("_")[1].split(".")[0]
            rep_date = datetime.strptime(date_s, "%Y%m%d")

            rep = BloodTestReport(path.name, rep_name, rep_date)
            rep.set_by_antech_br_report(bt_report)
            t = to_df([rep]).T
            dfl.append(t)

        df = pd.concat(dfl, axis=1)
        print(df)
        df.to_csv(str(out_file))


if __name__ == "__main__":
    main()

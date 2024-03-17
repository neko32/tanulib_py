from unittest import TestCase, main
from tlib.cat.br_analysis import BloodTestReport
from pathlib import Path
from datetime import datetime


class CatBTAnalysisTest(TestCase):

    def test_blood_test_import_from_antech_report(self):
        bt_antech_file = Path(__file__).parent.\
            joinpath("testdata", "text", "cat_bt_antech.txt")

        if not bt_antech_file.exists():
            raise Exception(
                f"test input file not exists at {str(bt_antech_file)}")

        with open(str(bt_antech_file), "r") as fd:
            bt_report = fd.read()

        rep = BloodTestReport("tako", "test1", datetime.now())
        rep.set_by_antech_br_report(bt_report)


if __name__ == "__main__":
    main()

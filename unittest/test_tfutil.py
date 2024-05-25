from tlib.ml.tfutil import *
from unittest import TestCase, main
from pathlib import Path


class TFUtilTest(TestCase):

    def test_build_dev_plancement_report(self):
        fpath = Path(__file__).parent.parent.joinpath(
            "unittest", "testdata", "text", "tlibs_run.log")
        report = build_device_placement_report(str(fpath))
        self.assertTupleEqual(report.shape, (48, 2))


if __name__ == "__main__":
    main()

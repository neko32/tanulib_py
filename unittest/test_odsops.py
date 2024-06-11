from tlib.office.ss_ops import *
from unittest import TestCase, main
from pathlib import Path


class ODSOpsTest(TestCase):

    def test_odsops(self):

        test_ods_file = Path("/tmp/test.ods")
        if test_ods_file.exists():
            test_ods_file.unlink()

        testods_path = Path(__file__).parent.parent.joinpath(
            "unittest", "testdata", "csv", "sample_ss.ods")
        ods = SpreadSheetOps(str(testods_path), SpreadSheetFormat.ODS)
        self.assertEqual(ods.get_num_sheets(), 2)
        ods.switch_sheet_view(0)
        self.assertEqual(ods.find_first_empty_cell_in_col('A', 1), 9)
        ods.switch_sheet_view(1)
        self.assertEqual(ods.find_first_empty_cell_in_col('A', 1), 9)
        ods.switch_sheet_view(0)
        self.assertEqual(ods.gets("A", 6), "2024-01-23")
        self.assertEqual(ods.gets("B", 6), "pm")
        self.assertEqual(ods.geti("D", 6), 65)
        new_row = [
            "2024-01-25",
            "am",
            "木",
            "",
        ]
        ods.insert_row(new_row)
        ods.persist(str(test_ods_file))
        self.assertTrue(test_ods_file.exists())


if __name__ == "__main__":
    main()

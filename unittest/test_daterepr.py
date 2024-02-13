from unittest import TestCase, main
from tlib.dateutil import *

class DateReprTest(TestCase):

    def test_cur_datetime_as_std_fmt(self):
        cur_date_notz_nossec = cur_datetime_as_std_fmt_str()
        print(cur_date_notz_nossec)
        self.assertTrue("T" in cur_date_notz_nossec)
        cur_date_z_nossec = cur_datetime_as_std_fmt_str(with_tz = True)
        print(cur_date_z_nossec)
        cur_date_z_ssec = cur_datetime_as_std_fmt_str(with_tz = True, with_ssec = True)
        print(cur_date_z_ssec)
        cur_date_noz_ssec = cur_datetime_as_std_fmt_str(with_ssec = True)
        print(cur_date_noz_ssec)
        cur_date_not = cur_datetime_as_std_fmt_str(with_t = False)
        print(cur_date_not)
        cur_date_dsep_tsep = cur_datetime_as_std_fmt_str(date_delimitor = '/', time_delimitor = '_')
        print(cur_date_dsep_tsep)
        cur_date_dsep_tsep_full = cur_datetime_as_std_fmt_str(date_delimitor = '/', time_delimitor = '_', with_tz = True, with_ssec = True)
        print(cur_date_dsep_tsep_full)


if __name__ == "__main__":
    main()


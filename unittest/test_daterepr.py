from unittest import TestCase, main
from tlib.dateutil import *
from zoneinfo import ZoneInfo

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
        cur_date_jst = cur_datetime_as_std_fmt_str(date_delimitor = '/', time_delimitor = '_', with_tz = True, with_ssec = True, timezone = datetime.timezone(datetime.timedelta(hours = 9), name = "JST"))
        print(cur_date_jst)

    def test_get_datetime_as_std_fmt_str(self):
        date_s = get_datetime_as_std_fmt_str(2020, 3, 17, 11, 28, 35,  '-', ':', True, True, False, ZoneInfo("America/New_York"))
        date = datetime.datetime.strptime(date_s, "%Y-%m-%dT%H:%M:%S%z")
        self.assertEqual(date.year, 2020)
        self.assertEqual(date.month, 3)
        self.assertEqual(date.day, 17)
        self.assertEqual(date.hour, 11)
        self.assertEqual(date.minute, 28)
        self.assertEqual(date.second, 35)
        



if __name__ == "__main__":
    main()


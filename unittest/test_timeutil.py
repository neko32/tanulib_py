from tlib.dateutil.timeutil import *
from unittest import TestCase, main
import time


class TimeUtilTest(TestCase):

    def test_timer_get_laptime(self):
        tm = Timer()
        tm.start()
        time.sleep(2.5)
        tm.stop()
        self.assertEqual(tm.hour, 0.)
        self.assertEqual(tm.min, 0.)
        self.assertEqual(tm.sec, 2.)
        self.assertTrue(tm.msec >= 45 and tm.msec <= 55.)

    def test_timer_wrong_ops_in_wrong_state(self):
        tm = Timer()
        tm.start()
        with self.assertRaises(Exception):
            tm.start()
        
        tm = Timer()
        with self.assertRaises(Exception):
            tm.stop()

    def test_default_value(self):
        tm = Timer()
        self.assertEqual(tm.hour, 0.)
        self.assertEqual(tm.min, 0.)
        self.assertEqual(tm.sec, 0.)
        self.assertEqual(tm.msec, 0.)
        


if __name__ == "__main__":
    main()

from unittest import TestCase, main
from tlib.core.linux import *
import platform
from pandas import DataFrame


class LinuxTest(TestCase):

    def test_lsb_release(self):
        if platform.system().lower().startswith('linux'):
            lsb = LSBInfo()
            self.assertTrue(len(lsb.distributor_id) > 0)
            self.assertTrue(len(lsb.description) > 0)
            self.assertTrue(len(lsb.release) > 0)
            self.assertTrue(len(lsb.codename) > 0)
        else:
            print(
                'non-linux env. skipping this test as this test depends on lsb_release command.')

    def test_ss_tcp_udp_established(self):
        ss_out = ss_tcp_udp_established()
        print(ss_out)

    def test_is_cmd_available(self):
        self.assertTrue(is_cmd_available('cat'))
        self.assertFalse(is_cmd_available('takoikatako'))


if __name__ == "__main__":
    main()

from unittest import TestCase, main
from tlib.core import LSBInfo
import platform

class LinuxTest(TestCase):

    def test_lsb_release(self):
        if platform.system().lower().startswith('linux'):
            lsb = LSBInfo()
            self.assertTrue(len(lsb.distributor_id) > 0)
            self.assertTrue(len(lsb.description) > 0)
            self.assertTrue(len(lsb.release) > 0)
            self.assertTrue(len(lsb.codename) > 0)
        else:
            print('non-linux env. skipping this test as this test depends on lsb_release command.')
        


if __name__ == "__main__":
    main()
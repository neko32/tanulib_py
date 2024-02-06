from unittest import TestCase, main
from tlib.datautil.hash import *

class HashTest(TestCase):

    def test_md5_from_str(self):
        ipt = "tako neko poko 37"
        b_md5, hexs_md5 = md5_from_str(ipt)
        self.assertEqual(hexs_md5, "2c7d0d52f027a23d974016f710c3b648")
        self.assertEqual(b_md5.hex(), hexs_md5)
        
    def test_md5_from_byte(self):
        ipt = "tako neko poko 37"
        b_md5, hexs_md5 = md5_from_str(ipt)
        self.assertEqual(hexs_md5, "2c7d0d52f027a23d974016f710c3b648")
        self.assertEqual(b_md5.hex(), hexs_md5)

    def test_md5_from_file(self):
        fpath = "./testdata/text/plain.txt"
        b_md5, hexs_md5 = md5_from_file(fpath)
        self.assertEqual(hexs_md5, "010f2f225d7e05ce8357dcd0736d8b76")
        self.assertEqual(b_md5.hex(), hexs_md5)




    


if __name__ == "__main__":
    main()
from unittest import TestCase, main
from tlib.datautil.hash import *


class HashTest(TestCase):

    def test_md5_from_str(self):
        ipt = "tako neko poko 37"
        b_md5 = md5_from_str(ipt)
        hexs_md5 = to_hex(b_md5)
        self.assertEqual(hexs_md5, "2c7d0d52f027a23d974016f710c3b648")
        self.assertEqual(b_md5.hex(), hexs_md5)

    def test_md5_from_byte(self):
        ipt = b"tako neko poko 37"
        b_md5 = md5_from_bytes(ipt)
        hexs_md5 = to_hex(b_md5)
        self.assertEqual(hexs_md5, "2c7d0d52f027a23d974016f710c3b648")
        self.assertEqual(b_md5.hex(), hexs_md5)

    def test_md5_from_file(self):
        fpath = "./testdata/text/plain.txt"
        b_md5 = md5_from_file(fpath)
        hexs_md5 = to_hex(b_md5)
        self.assertEqual(hexs_md5, "010f2f225d7e05ce8357dcd0736d8b76")
        self.assertEqual(b_md5.hex(), hexs_md5)

    def test_sha2_256_from_str(self):
        ipt = "tako neko poko 37"
        b_sha256 = sha2_256_from_str(ipt)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "1f366a9a660ac1c84f665defd37146861a55ee4a4b1e3af3e3d9b7b98f95d8ab"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)

    def test_sha2_256_from_byte(self):
        ipt = b"tako neko poko 37"
        b_sha256 = sha2_256_from_bytes(ipt)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "1f366a9a660ac1c84f665defd37146861a55ee4a4b1e3af3e3d9b7b98f95d8ab"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)

    def test_sha2_256_from_file(self):
        fpath = "./testdata/text/plain.txt"
        b_sha256 = sha2_256_from_file(fpath)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "20a38d3ba13f9ba2331fbec53542ac7ef5800c880215db28be272da92753146b"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)

    def test_sha3_256_from_str(self):
        ipt = "tako neko poko 37"
        b_sha256 = sha3_256_from_str(ipt)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "14066fc9c591e95e5a1e17a820ba9fd1120bae53e4c9208737a12246e1e1ad91"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)

    def test_sha3_256_from_byte(self):
        ipt = b"tako neko poko 37"
        b_sha256 = sha3_256_from_bytes(ipt)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "14066fc9c591e95e5a1e17a820ba9fd1120bae53e4c9208737a12246e1e1ad91"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)

    def test_sha3_256_from_file(self):
        fpath = "./testdata/text/plain.txt"
        b_sha256 = sha3_256_from_file(fpath)
        hexs_sha256 = to_hex(b_sha256)
        self.assertEqual(
            hexs_sha256,
            "cc92aa9aeb491f09aee76f785d8c7047a2c33c8dda5f75b25d69693fb51002ac"
        )
        self.assertEqual(b_sha256.hex(), hexs_sha256)


if __name__ == "__main__":
    main()

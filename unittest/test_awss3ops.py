from unittest import TestCase, main
from tlib.aws import s3ops
import os


class AWSS3OpsTest(TestCase):

    def setUp(self):
        self.bucket_name = "testbk1"
        self.bucket_name2 = "testbk2"
        os.environ['ENV'] = 'local_ut'

    def tearDown(self) -> None:
        self.assertTrue(s3ops.delete_s3_bucket(self.bucket_name))
        return super().tearDown()

    def test_s3_basic_ops(self):
        test_json1_fpath = "./testdata/json/test_simple.json"
        test_json1_key = "testsimple1"
        rez = s3ops.create_s3_bucket(self.bucket_name, s3ops.ACLTypes.private)
        print(rez)

        with open(test_json1_fpath, 'r') as fp:
            test_json1_data = bytes(fp.read(), 'utf-16')

        put_rez = s3ops.put_object_to_s3_bucket(
            f"{self.bucket_name}",
            s3ops.ACLTypes.private,
            test_json1_key, test_json1_data)
        print(put_rez)

        lsrez = s3ops.list_object_in_s3_bucket(f"{self.bucket_name}")
        for ks in lsrez.list_key_and_size():
            print(f"{ks.key}:{ks.size}")
            self.assertTrue(s3ops.delete_object_from_s3_bucket(
                self.bucket_name, ks.key))

    def test_list_s3_buckets(self):
        s3ops.create_s3_bucket(self.bucket_name, s3ops.ACLTypes.private)
        s3ops.create_s3_bucket(self.bucket_name2, s3ops.ACLTypes.private)
        names = ["testbk1", "testbk2"]

        for (name, dt) in s3ops.list_buckets().get_list():
            self.assertTrue(name in names)
            self.assertEqual(type(dt).__name__, "datetime")

        self.assertTrue(s3ops.delete_s3_bucket(self.bucket_name2))


if __name__ == '__main__':
    main()

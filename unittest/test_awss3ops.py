from unittest import TestCase, main
from tlib.aws import s3ops
import os

class AWSS3OpsTest(TestCase):

    def setUp(self):
        os.environ['ENV'] = 'local_ut'

    def test_s3_basic_ops(self):
        bucket_name = "testbk1"
        bucket_created = False
        try:
            rez = s3ops.create_s3_bucket(bucket_name, s3ops.ACLTypes.private)
            print(rez)
            bucket_created = True
            
            self.assertTrue(s3ops.delete_s3_bucket(bucket_name))
            bucket_created = False
            
        except Exception as e:
            print(f"error occurred - {e}")
            if bucket_created:
                s3ops.delete_s3_bucket(bucket_name)


if __name__ == '__main__':
    main()

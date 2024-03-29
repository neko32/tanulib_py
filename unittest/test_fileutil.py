from unittest import TestCase, main
from tlib.fileutil import *
from tlib.datautil import gen_rand_alnum_str
from os.path import exists
from os import mkdir, environ
from pathlib import Path
import csv


class FileutilTest(TestCase):

    def test_split_filename_postfix_normal(self):
        fname = "testfile.txt"
        sp = split_filename_postfix(fname)
        self.assertEqual(sp[0], "testfile")
        self.assertEqual(sp[1], "txt")

    def test_split_filename_postfix_multidots(self):
        fname = "testfile.txt.tar.gz"
        sp = split_filename_postfix(fname)
        self.assertEqual(sp[0], "testfile.txt.tar")
        self.assertEqual(sp[1], "gz")

    def test_split_filename_postfix_nopostfix(self):
        fname = "testfile"
        sp = split_filename_postfix(fname)
        self.assertEqual(sp[0], "testfile")
        self.assertIsNone(sp[1])

    def test_rmdir_file(self):
        test_dir_name = gen_rand_alnum_str(16)
        test_dir = f"/tmp/{test_dir_name}"
        test_dir_files = [
            f"{test_dir}/{gen_rand_alnum_str(16)}" for _ in range(10)]

        mkdir(test_dir)

        for f in test_dir_files:
            with open(f, "w") as fp:
                fp.write("test")

        n_success, n_fail = rmdir_and_files(test_dir)
        self.assertEqual(n_success, 10)
        self.assertEqual(n_fail, 0)
        self.assertFalse(exists(test_dir))

    def test_gen_imagefiles_summary(self):
        test_csv_name = gen_rand_alnum_str(16)
        test_file = f"/tmp/{test_csv_name}.csv"

        img_files_dir = "./testdata/img"
        gen_image_files_summary(img_files_dir, test_file)

        self.assertTrue(exists(test_file))

        with open(test_file, 'r') as fp:
            csv_r = csv.reader(fp)
            for i, row in enumerate(csv_r):
                if i == 0:
                    self.assertListEqual(
                        row,
                        [
                            'filename',
                            'postfix',
                            'width',
                            'height',
                            'channel',
                            'magic'
                        ]
                    )
                else:
                    self.assertEqual(len(row), 6)

        remove(test_file)

    def test_is_JFIF_img_file(self):
        broken_file = "./testdata/img/broken_img.jpg"
        valid_file = "./testdata/img/cat_img1.jpg"
        self.assertTrue(is_JFIF_img_file(valid_file))
        self.assertFalse(is_JFIF_img_file(broken_file))

    def test_get_dirs_files(self):
        tmp_dir = environ["HOME_TMP_DIR"]
        tmp_dir = str(Path(tmp_dir).joinpath("test_ftl"))
        test_files_at_d1 = ["file.txt", "file2.txt"]
        test_files_at_d2 = ["file3.txt", "file4.txt"]
        test_files_at_d3 = ["file5.txt"]
        test_d1 = ["test_fileutil_d1", "test_fileutil_d2"]
        test_d2 = ["test_fileutil_d3"]

        path = Path(tmp_dir)
        path.mkdir()
        for d in test_d1:
            path = Path(tmp_dir).joinpath(d)
            path.mkdir()
        for d in test_d2:
            path = Path(tmp_dir).joinpath(test_d1[0], d)
            path.mkdir()
        for f in test_files_at_d1:
            path = Path(tmp_dir).joinpath(test_d1[0], f)
            path.touch()
        for f in test_files_at_d2:
            path = Path(tmp_dir).joinpath(test_d1[1], f)
            path.touch()
        for f in test_files_at_d3:
            path = Path(tmp_dir).joinpath(test_d1[0], test_d2[0], f)
            path.touch()

        dirs, files = list_files_and_dirs(
            str(Path(tmp_dir)),
            glob_str="**/*"
        )
        test_files = test_files_at_d1 + test_files_at_d2 + test_files_at_d3
        test_dirs = test_d1 + test_d2
        for f in files:
            self.assertTrue(any(list(map(lambda x: x in f, test_files))))
        for d in dirs:
            self.assertTrue(any(list(map(lambda x: x in d, test_dirs))))

        # cleanup

        for f in test_files_at_d1:
            path = Path(tmp_dir).joinpath(test_d1[0], f)
            path.unlink()
        for f in test_files_at_d2:
            path = Path(tmp_dir).joinpath(test_d1[1], f)
            path.unlink()
        for f in test_files_at_d3:
            path = Path(tmp_dir).joinpath(test_d1[0], test_d2[0], f)
            path.unlink()
        for d in test_d2:
            path = Path(tmp_dir).joinpath(test_d1[0], d)
            path.rmdir()
        for d in test_d1:
            path = Path(tmp_dir).joinpath(d)
            path.rmdir()
        path = Path(tmp_dir)
        path.rmdir()


if __name__ == "__main__":
    main()

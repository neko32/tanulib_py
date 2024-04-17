from unittest import TestCase, main
from tlib.graphics.img_info import *
from pathlib import Path


class ImgInfoTest(TestCase):

    def test_exifinfo(self):

        testimg_path = str(Path(__file__).parent.joinpath(
            "testdata", "img", "cat_img1.jpg"))
        exif = get_exif_data(testimg_path)
        self.assertEqual(exif["JFIF Version"], "1.02")
        self.assertEqual(exif["X Resolution"], "1")
        self.assertEqual(exif["File Name"], "cat_img1.jpg")

    def test_nofileexist(self):

        testimg_path = "/tako/tako.png"
        with self.assertRaises(Exception):
            get_exif_data(testimg_path)


if __name__ == "__main__":
    main()

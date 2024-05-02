from unittest import TestCase, main
from tlib.graphics.img_info import *
from tlib.graphics.graphics import imread_wrapper
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

        testimg_path = str(Path(__file__).parent.joinpath(
            "testdata", "img", "cat_img100000.jpg"))
        with self.assertRaises(Exception):
            get_exif_data(testimg_path)

    def test_aspect_ratio(self):

        self.assertTupleEqual(aspect_ratio(972., 560.), (243., 140.))
        testimg_path = str(Path(__file__).parent.joinpath(
            "testdata", "img", "nekovation640480.png"))
        img = imread_wrapper(testimg_path)
        self.assertTupleEqual(aspect_ratio_of_image(img), (4, 3))
        self.assertTrue(is_horizontal_image_by_aspect_ratio(img))
        testimg_path2 = str(Path(__file__).parent.joinpath(
            "testdata", "img", "broken_img.jpg"))
        img2 = imread_wrapper(testimg_path2)
        self.assertTupleEqual(aspect_ratio_of_image(img2), (14., 15.))
        self.assertFalse(is_horizontal_image_by_aspect_ratio(img2))


if __name__ == "__main__":
    main()

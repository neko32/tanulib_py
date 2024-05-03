import cv2
from tlib.datautil import gen_rand_alnum_str
from tlib.fileutil import rmdir_and_files
from tlib.graphics import *
from unittest import TestCase, main
from os import remove, mkdir
from os.path import exists
from pathlib import Path
import magic


class GrapchicsTest(TestCase):

    def test_imread_wrapper(self):
        good_path = "./testdata/img/cat_img1.jpg"
        bad_path = "./testdata/img/sonnan_sonzai_shineyo.jpg"
        f = imread_wrapper(good_path, cv2.IMREAD_GRAYSCALE)
        self.assertTrue(is_grayscale(f))
        with self.assertRaises(Exception):
            imread_wrapper(bad_path)

    def gen_dest_fname(self, length: int = 16, postfix: str = "jpg") -> str:
        return f"/tmp/{gen_rand_alnum_str(length)}.{postfix}"

    def test_resize_img(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname()

        if exists(dest_img_path):
            remove(dest_img_path)

        resize_img(test_img_path, dest_img_path, 100, 115)
        self.assertTrue(exists(dest_img_path))
        resized = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        h, w = resized.shape[:2]
        self.assertTrue(h == 115)
        self.assertTrue(w == 100)

        remove(dest_img_path)

    def test_persist_as_gray_image(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname()

        if exists(dest_img_path):
            remove(dest_img_path)

        self.assertTrue(persist_as_gray_image(test_img_path, dest_img_path))
        must_be_gray = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        self.assertTrue(is_grayscale(must_be_gray))
        remove(dest_img_path)

    def test_copy_image_from_jpg_to_png(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname(postfix="png")
        self.assertTrue(copy_img(test_img_path, dest_img_path))
        magicwords = magic.from_file(dest_img_path)
        self.assertTrue("png" in magicwords.lower())
        remove(dest_img_path)

    def test_copy_image_from_png_to_jpg(self):
        test_img_path = "./testdata/img/nekovation640480.png"
        dest_img_path = self.gen_dest_fname(postfix="jpg")
        self.assertTrue(copy_img(test_img_path, dest_img_path))
        magicwords = magic.from_file(dest_img_path)
        self.assertTrue("jpeg" in magicwords.lower())
        remove(dest_img_path)

    def test_resize_all_imgs(self):
        test_img_path = "./testdata/img"
        dir_name = gen_rand_alnum_str(16)
        dest_img_path = f"/tmp/{dir_name}"
        mkdir(dest_img_path)
        self.assertEqual(resize_all_imgs(
            test_img_path, dest_img_path, 200, 150), 4)

        rmdir_and_files(dest_img_path)

    def test_affine_transform(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)
        warped = affine_transform(input_img, 1, 45)
        self.assertTrue(persist_img(warped, "/tmp/affine.jpg"))

    def test_shift_invariance_same_grayscale_imgs(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        self.assertTrue(
            is_shift_invarient_for_grayscale_imgs(input_img, input_img))

    def test_shift_invariance_rotate_case(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        rotated = cv2.rotate(input_img, cv2.ROTATE_90_CLOCKWISE)
        self.assertTrue(
            is_shift_invarient_for_grayscale_imgs(input_img, rotated))

    def test_shift_invariance_sheared_with_blackfill_case(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        sheared = affine_transform(input_img, 1, 45)
        self.assertFalse(
            is_shift_invarient_for_grayscale_imgs(input_img, sheared))

    def test_shift_invariance_non_grayscale_input(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)
        input_img_grayed = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        with self.assertRaises(Exception):
            is_shift_invarient_for_grayscale_imgs(input_img, input_img)
        with self.assertRaises(Exception):
            is_shift_invarient_for_grayscale_imgs(input_img, input_img_grayed)
        with self.assertRaises(Exception):
            is_shift_invarient_for_grayscale_imgs(input_img_grayed, input_img)

    def test_conv_bgr_to_hsv(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)
        hsv_img = conv_from_bgr_to_hsv(input_img)
        self.assertFalse(np.array_equal(input_img, hsv_img))

    def test_minmax_pix_loc(self):
        img = np.array(
            [
                [0, 2, 1],
                [1, 1, 0],
                [1, 2, 0]
            ],
            dtype=np.uint8)

        min_expected = [(0, 0), (1, 2), (2, 2)]
        max_expected = [(0, 1), (2, 1)]
        minposs, maxposs = get_minmax_pix_loc(img)
        self.assertEqual(minposs, min_expected)
        self.assertEqual(maxposs, max_expected)

    def test_is_highcontrast(self):
        col1_1 = (60, 30, 20)
        col1_2 = (180, 200, 255)
        col2_1 = (100, 200, 220)
        col2_2 = (180, 200, 255)
        self.assertTrue(is_high_contract(col1_1, col1_2, True))
        self.assertFalse(is_high_contract(col2_1, col2_2, True))

    def test_conv_to_opencv_hue(self):
        hue = 40
        self.assertTrue(conv_to_opencv_hue(hue), 20.)

    def test_conv_to_opencv_satval(self):
        sat = 34.
        v = 88.
        self.assertTrue(conv_to_opencv_sat_val(sat), 86.7)
        self.assertTrue(conv_to_opencv_sat_val(v), 224.4)

    def test_image2d_to_1d(self):
        input_img_path = str(Path(__file__).parent.joinpath(
            "testdata", "img", "cat_img1.jpg"))
        img = imread_wrapper(input_img_path)
        sdi, stride = from_2dimage_to_1dimage(img)
        print(img.shape)
        print(stride)
        b, g, r,_ = get_pixel(img, 200, 130)
        print(r, g, b)
        b2 = sdi[stride * 130 + 200 * 3]
        g2 = sdi[stride * 130 + 200 * 3 + 1]
        r2 = sdi[stride * 130 + 200 * 3 + 2]
        self.assertEqual(b, b2)
        self.assertEqual(g, g2)
        self.assertEqual(r, r2)


if __name__ == "__main__":
    main()

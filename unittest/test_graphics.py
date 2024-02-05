import cv2
from tlib.datautil import gen_rand_alnum_str
from tlib.fileutil import rmdir_and_files
from tlib.graphics import *
from unittest import TestCase, main
from os import remove, mkdir
from os.path import exists
import magic

class GrapchicsTest(TestCase):

    def gen_dest_fname(self, length:int = 16, postfix:str = "jpg") -> str:
        return f"/tmp/{gen_rand_alnum_str(length)}.{postfix}"

    def test_resize_img(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname()

        if exists(dest_img_path):
            remove(dest_img_path)

        self.assertTrue(resize_img(test_img_path, dest_img_path, 100, 115))
        self.assertTrue(exists(dest_img_path))
        resized = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        h, w = resized.shape[:2]
        self.assertTrue(h == 115)
        self.assertTrue(w == 100)

        remove(dest_img_path)

    def test_to_gray_image(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname()

        if exists(dest_img_path):
            remove(dest_img_path)

        self.assertTrue(to_gray_image(test_img_path, dest_img_path))
        must_be_gray = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        self.assertTrue(is_grayscale(must_be_gray))
        remove(dest_img_path)

    def test_copy_image_from_jpg_to_png(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname(postfix = "png")
        self.assertTrue(copy_img(test_img_path, dest_img_path))
        magicwords = magic.from_file(dest_img_path)
        self.assertTrue("png" in magicwords.lower())
        remove(dest_img_path)

    def test_copy_image_from_png_to_jpg(self):
        test_img_path = "./testdata/img/nekovation640480.png"
        dest_img_path = self.gen_dest_fname(postfix = "jpg")
        self.assertTrue(copy_img(test_img_path, dest_img_path))
        magicwords = magic.from_file(dest_img_path)
        self.assertTrue("jpeg" in magicwords.lower())
        remove(dest_img_path)

    def test_resize_all_imgs(self):
        test_img_path = "./testdata/img"
        dir_name = gen_rand_alnum_str(16)
        dest_img_path = f"/tmp/{dir_name}"
        mkdir(dest_img_path)
        self.assertEqual(resize_all_imgs(test_img_path, dest_img_path, 200, 150), 2)
        
        rmdir_and_files(dest_img_path)

    def test_affine_transform(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)
        warped = affine_transform(input_img, 1, 45)
        self.assertTrue(persist_img(warped, "/tmp/affine.jpg"))

    def test_shift_invariance_same_grayscale_imgs(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        self.assertTrue(is_shift_invarient_for_grayscale_imgs(input_img, input_img))

    def test_shift_invariance_rotate_case(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        rotated = cv2.rotate(input_img, cv2.ROTATE_90_CLOCKWISE)
        self.assertTrue(is_shift_invarient_for_grayscale_imgs(input_img, rotated))

    def test_shift_invariance_sheared_with_blackfill_case(self):
        input_img_path = "./testdata/img/cat_img1.jpg"
        input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)
        sheared = affine_transform(input_img, 1, 45)
        self.assertFalse(is_shift_invarient_for_grayscale_imgs(input_img, sheared))

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



if __name__ == "__main__":
    main() 
        

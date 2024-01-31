import cv2
from tlib.datautil import gen_rand_alnum_str
from tlib.graphics import *
from unittest import TestCase, main
from os import remove
from os.path import exists

class GrapchicsTest(TestCase):

    def gen_dest_fname(self, length = 16) -> str:
        return f"/tmp/{gen_rand_alnum_str(length)}.jpg"

    def test_img_resize(self):
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

    def test_img_to_grayscale(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_img_path = self.gen_dest_fname()

        if exists(dest_img_path):
            remove(dest_img_path)

        self.assertTrue(to_gray_image(test_img_path, dest_img_path))
        must_be_gray = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        self.assertEqual(len(must_be_gray.shape), 2)

if __name__ == "__main__":
    main() 
        

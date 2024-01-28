import cv2
from tlib.datautil import gen_rand_alnum_str
from tlib.graphics import resize_img
from unittest import TestCase, main
from os import remove
from os.path import exists

class GrapchicsTest(TestCase):

    def test_img_resize(self):
        test_img_path = "./testdata/img/cat_img1.jpg"
        dest_name = gen_rand_alnum_str(16)
        dest_img_path = f"/tmp/{dest_name}.jpg"

        if exists(dest_img_path):
            remove(dest_img_path)

        self.assertTrue(resize_img(test_img_path, dest_img_path, 100, 115))
        self.assertTrue(exists(dest_img_path))
        resized = cv2.imread(dest_img_path, cv2.IMREAD_UNCHANGED)
        h, w = resized.shape[:2]
        self.assertTrue(h == 115)
        self.assertTrue(w == 100)
        

if __name__ == "__main__":
    main() 
        

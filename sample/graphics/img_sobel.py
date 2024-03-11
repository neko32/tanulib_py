from tlib.graphics import *
import cv2
import os
from os import remove
from os.path import exists


def main():
    tmp_home_dir = os.environ["HOME_TMP_DIR"]
    f_input_name = "../img/sample_img.jpg"
    f_output_name_x = f"{tmp_home_dir}/sobel_x_sample.jpg"
    f_output_name_y = f"{tmp_home_dir}/sobel_y_sample.jpg"

    if exists(f_output_name_x):
        remove(f_output_name_x)
    if exists(f_output_name_y):
        remove(f_output_name_y)

    img = imread_wrapper(f_input_name, cv2.IMREAD_GRAYSCALE)
    sobel_x = filter_by_SOBEL(
        img=img,
        output_img_depth=ImageDepthType.IMG_DEPTH_8UINT,
        order=SOBELOrder.ORDER_X
    )
    sobel_y = filter_by_SOBEL(
        img=img,
        output_img_depth=ImageDepthType.IMG_DEPTH_8UINT,
        order=SOBELOrder.ORDER_Y
    )
    try:
        cv2.imwrite(f_output_name_x, sobel_x)
        print(f"sobel filter X sample done. file written to {f_output_name_x}")
        cv2.imwrite(f_output_name_y, sobel_y)
        print(f"sobel filter Y sample done. file written to {f_output_name_y}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

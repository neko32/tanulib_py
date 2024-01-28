import cv2
def resize_img(src_path:str, dest_path:str, new_width:int, new_height:int):
    buf = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(buf, [new_width, new_height])
    # [TODO] derive option best by postfix of file
    return cv2.imwrite(dest_path, resized, [cv2.IMWRITE_JPEG_QUALITY, 100])
    
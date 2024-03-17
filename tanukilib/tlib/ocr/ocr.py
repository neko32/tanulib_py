from tlib.core import exec_cmd


def do_ocr_scan(img_path: str):
    """
    Do OCR scan using tesseract command line.
    pytesseract accuracy was not great at all..
    """
    ret_code, stdout, _ = exec_cmd(["tesseract", img_path, "stdout"])
    if ret_code != 0:
        raise Exception(f"failed to perform OCR for {img_path}")
    return stdout

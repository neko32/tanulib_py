from tlib.graphics.movie import *
from tlib.graphics.video import *
import cv2


def main():
    for idx in range(11):
        try:
            vt = VideoCapturer(idx, cv2.CAP_ANY)
            print(vt.device_test())
        except Exception:
            print(f"device idx {idx} is not available or doesn't exist")


if __name__ == "__main__":
    main()

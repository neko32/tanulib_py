import cv2
from typing import List
from tlib.graphics.movie import Effecter


class VideoAttribs:
    def __init__(self, vt: cv2.VideoCapture):
        self._frame_width = vt.get(cv2.CAP_PROP_FRAME_WIDTH)
        self._frame_height = vt.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self._fps = vt.get(cv2.CAP_PROP_FPS)
        self._fourcc = vt.get(cv2.CAP_PROP_FOURCC)
        self._format = vt.get(cv2.CAP_PROP_FORMAT)
        self._brightness = vt.get(cv2.CAP_PROP_BRIGHTNESS)
        self._contrast = vt.get(cv2.CAP_PROP_CONTRAST)
        self._saturation = vt.get(cv2.CAP_PROP_SATURATION)
        self._hue = vt.get(cv2.CAP_PROP_HUE)
        self._gain = vt.get(cv2.CAP_PROP_GAIN)
        self._exposure = vt.get(cv2.CAP_PROP_EXPOSURE)
        self._autofocus = vt.get(cv2.CAP_PROP_AUTOFOCUS)
        self._sharpness = vt.get(cv2.CAP_PROP_SHARPNESS)
        self._zoom = vt.get(cv2.CAP_PROP_ZOOM)
        self._pan = vt.get(cv2.CAP_PROP_PAN)
        self._tilt = vt.get(cv2.CAP_PROP_TILT)
        self._auto_exposure = vt.get(cv2.CAP_PROP_AUTO_EXPOSURE)

    @property
    def frame_width(self) -> float:
        return self._frame_width

    @property
    def frame_height(self) -> float:
        return self._frame_height

    @property
    def fps(self) -> float:
        return self._fps

    @property
    def fourcc(self) -> float:
        return self._fourcc

    @property
    def format(self) -> float:
        return self._format

    @property
    def brightness(self) -> float:
        return self._brightness

    @property
    def contrast(self) -> float:
        return self._contrast

    @property
    def saturation(self) -> float:
        return self._saturation

    @property
    def hue(self) -> float:
        return self._hue

    @property
    def gain(self) -> float:
        return self._gain

    @property
    def explosure(self) -> float:
        return self._exposure

    @property
    def auto_focus(self) -> float:
        return self._auto_focus

    @property
    def sharpness(self) -> float:
        return self._sharpness

    @property
    def zoom(self) -> float:
        return self._zoom

    @property
    def pan(self) -> float:
        return self._pan

    @property
    def tilt(self) -> float:
        return self._tilt

    @property
    def auto_exposure(self) -> float:
        return self._auto_exposure

    def summary(self) -> List[str]:
        buf = []
        buf.append(f"FRAME_WIDTH:{self._frame_width}")
        buf.append(f"FRAME_HEIGHT:{self._frame_height}")
        buf.append(f"FPS:{self._fps}")
        buf.append(f"FOURCC:{self._fourcc}")
        buf.append(f"FORMAT:{self._format}")
        buf.append(f"BRIGHTNESS:{self._brightness}")
        buf.append(f"CONTRAST:{self._contrast}")
        buf.append(f"SATURATION:{self._saturation}")
        buf.append(f"HUE:{self._hue}")
        buf.append(f"GAIN:{self._gain}")
        buf.append(f"EXPOSURE:{self._exposure}")
        buf.append(f"AUTOFOCUS:{self._autofocus}")
        buf.append(f"SHARPNESS:{self._sharpness}")
        buf.append(f"ZOOM:{self._zoom}")
        buf.append(f"PAN:{self._pan}")
        buf.append(f"TILT:{self._tilt}")
        buf.append(f"AUTOEXPOSURE:{self._auto_exposure}")
        return buf


class VideoCapturer:

    def __init__(self, index: int, api_pref: int):
        self.index = index
        self.api_pref = api_pref
        self.video_attribs = None

    def device_test(self) -> str:
        vt = cv2.VideoCapture(self.index, self.api_pref)
        attribs = VideoAttribs(vt)

        return "\n".join(
            [
                f"INDEX:{self.index}",
                f"API_PREF:{self.api_pref}"
            ] + attribs.summary()
        )

    def capture(
            self,
            wnd_name: str,
            effects: List[Effecter]) -> None:
        vt = cv2.VideoCapture(self.index, self.api_pref)
        self.video_attribs = VideoAttribs(vt)

        if not vt.isOpened():
            raise Exception(
                f"Video Capture with {self.index} + \
                    {self.api_pref} start failure")

        while True:
            read_success, r = vt.read()
            if not read_success:
                break

            for effect in effects:
                r = effect.process(r, vt)

            cv2.imshow(wnd_name, r)

            key = cv2.waitKey(30) & 0xFF
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        vt.release()

import time
import math


class Timer:
    """Timer to provide lap time calc feature"""

    def __init__(self):
        self._starttime = None
        self._endtime = None
        self.is_running = False
        self._hour = None
        self._min = None
        self._sec = None
        self._msec = None

    def start(self) -> None:
        """Start the timer to calcurate the wraptime"""
        if self.is_running:
            raise Exception("already running. stop current timer first")
        self._starttime = time.time()
        self.is_running = True

    def stop(self) -> None:
        """Stop the timer to calcurate the wraptime"""
        if not self.is_running:
            raise Exception("timer not running")
        self._endtime = time.time()
        self.is_running = False
        ms, v = math.modf(self._endtime - self._starttime)
        self._msec = math.floor(ms * 100)
        self._hour = math.floor(v / 3600)
        self._min = math.floor(((v % 3600) / 60))
        self._sec = math.floor(v % 60)

    @property
    def hour(self) -> float:
        return self._hour if self._hour is not None else 0.

    @property
    def min(self) -> float:
        return self._min if self._min is not None else 0.

    @property
    def sec(self) -> float:
        return self._sec if self._sec is not None else 0.

    @property
    def msec(self) -> float:
        return self._msec if self._msec is not None else 0.

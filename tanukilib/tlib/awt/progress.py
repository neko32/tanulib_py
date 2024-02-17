from typing import Callable, Any
from time import perf_counter
import threading

class ProgressTrackTrait:

    def __init__(self, start:float, end:float, callback:Callable[[float, float], Any], verbose:bool = False):
        self.current = start
        self.end = end
        self.callback = callback
        self.start_time = -1.
        self.done = False
        self.lock = threading.Lock()
        self.verbose = verbose

    def progress(self, delta:float) -> bool:
        if self.done:
            return False
        
        with self.lock:
            if self.start_time == -1.:
                self.start_time = perf_counter() 
            prev = self.current
            self.current += delta 
            if self.verbose:
                print(f"{prev} -> {self.current}(+{delta}) [END:{self.end}]")
            if self.current >= self.end and not self.done:
                self.done = True
                self.callback(self.current, perf_counter() - self.start_time)

        return True

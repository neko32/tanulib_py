from tlib.awt.progress import *
import random
from unittest import TestCase, main
import time

class ProgressTest(TestCase):

    def _show_done(self, amt:float, elapsed:float) -> None:
        print(f"mock work done. progress ${amt}% and took {elapsed} msecs.")
        self.done = True

    def _add_progess(self, progress_track:ProgressTrackTrait):
        while True:
            rand_progress = random.random() * 10
            if not progress_track.progress(rand_progress):
                break
            if progress_track.done:
                break
            sleep_dr = random.random() * 1000
            time.sleep(sleep_dr / 1000) 

    def testProgressTrackTrait(self):

        pt = ProgressTrackTrait(0., 100., self._show_done, True)
        threads = []
        for _ in range(5):
            threads.append(threading.Thread(target = self._add_progess, args = [pt]))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertTrue(self.done)

if __name__ == "__main__":
    main()
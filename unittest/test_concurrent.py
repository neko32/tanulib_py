from tlib.core.concurrent import *
from unittest import TestCase, main
import time
import asyncio


class ConcurrentTest(TestCase):

    async def _heavy_ops(self, wait_time:int):
        print("starting..")
        await asyncio.sleep(wait_time)
        return "hi there"

    def test_exec_with_text_spinner(self):
        heavy = self._heavy_ops(2)
        st = time.perf_counter()
        result = exec_with_text_spinner(heavy, "wait a bit man..")
        end = time.perf_counter()
        self.assertEqual(result, "hi there")
        self.assertTrue(end - st >= 2.)



if __name__ == "__main__":
    main()
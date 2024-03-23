import asyncio
import sys
import itertools
from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


async def _show_text_spin(msg: str) -> None:
    """
    show spinner while showing msg
    """
    write, flush = sys.stdout.write, sys.stdout.flush
    write(f"{msg} ")
    for c in itertools.cycle('|/-\\'):
        write(c)
        flush()
        write('\x08')
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print("cancelled")
            break
    write('\x08')


def exec_with_text_spinner(func: Callable[[T], U], msg: str, timeout: int = -1) -> U:
    """
    execute specified func. While running the func, msg is shown with spinner
    """
    loop = asyncio.get_event_loop()
    spinner = _show_text_spin(msg)
    done, _ = loop.run_until_complete(asyncio.wait(
        [spinner, func], return_when=asyncio.FIRST_COMPLETED))
    for done_task in done:
        result = done_task.result()
    for task in asyncio.all_tasks(loop):
        if not task.cancelled():
            task.cancel()
    return result

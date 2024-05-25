import re
import pandas as pd
from tlib.fileutil.fileutil import read_file_as_stream


def build_device_placement_report(logfile: str) -> pd.DataFrame:
    """Build a report for device placement"""

    stream = read_file_as_stream(logfile)
    reg = re.compile(r"Executing op ([/:\w]+) in device ([/:\w]+)")

    col = ["ops", "device"]
    df = pd.DataFrame(columns=col)

    try:
        while True:
            line = next(stream)
            match = reg.search(line)
            if match is not None:
                groups = match.groups()
                ops = groups[0]
                device = groups[1]
                n = pd.DataFrame([[ops, device]], columns=col)
                df = pd.concat([df, n], ignore_index=True)

    except StopIteration:
        pass

    return df

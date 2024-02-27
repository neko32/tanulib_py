import datetime
from dateutil.tz import gettz


def cur_datetime_as_std_fmt_str(
    date_delimitor: str = '-',
    time_delimitor: str = ':',
    with_t: bool = True,
    with_tz: bool = False,
    with_ssec: bool = False,
    timezone: datetime.timezone = datetime.timezone.utc
) -> str:
    fmt = f"%Y{date_delimitor}%m{date_delimitor}%d"
    if with_t:
        fmt += "T"
    fmt += f"%H{time_delimitor}%M{time_delimitor}%S"
    if with_ssec:
        fmt += ".%f"
    if with_tz:
        fmt += "%z"
    return datetime.datetime.now(timezone).strftime(fmt)


def get_datetime_as_std_fmt_str(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    sec: int,
    date_delimitor: str = '-',
    time_delimitor: str = ':',
    with_t: bool = True,
    with_tz: bool = False,
    with_ssec: bool = False,
    timezone: datetime.timezone = datetime.timezone.utc
) -> str:
    fmt = f"%Y{date_delimitor}%m{date_delimitor}%d"
    if with_t:
        fmt += "T"
    fmt += f"%H{time_delimitor}%M{time_delimitor}%S"
    if with_ssec:
        fmt += ".%f"
    if with_tz:
        fmt += "%z"
    return datetime.datetime(
        year,
        month,
        day,
        hour,
        minute,
        sec,
        tzinfo=timezone
    ).strftime(fmt)


def from_epoch_to_datetime(epoch: int, tz_id: str) -> datetime.datetime:
    tz = gettz(tz_id)
    return datetime.datetime.fromtimestamp(epoch, tz)


def last_day_of_month(year: int, month: int) -> int:
    y = year + 1 if month == 12 else year
    m = 1 if month == 12 else month + 1
    date_nextmonth = datetime.date(year=y, month=m, day=1)
    date_the_month = date_nextmonth - datetime.timedelta(days=1)
    return date_the_month.day

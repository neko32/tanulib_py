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
    """
    Returns ISO-8601 date(time) formatted string for current datetime
    """
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
    """
    Returns ISO-8601 date(time) formatted string for specified datetime
    """
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
    """convert epoch time to datetime"""
    tz = gettz(tz_id)
    return datetime.datetime.fromtimestamp(epoch, tz)


def last_day_of_month(year: int, month: int) -> int:
    """get last day of the month"""
    y = year + 1 if month == 12 else year
    m = 1 if month == 12 else month + 1
    date_nextmonth = datetime.date(year=y, month=m, day=1)
    date_the_month = date_nextmonth - datetime.timedelta(days=1)
    return date_the_month.day


def from_yyyy_to_heisei_era(year: int) -> int:
    """convert western year to Japanese Heisei era year"""
    r = (year + 12) - 2000
    if r <= 0:
        raise ValueError("Heisei era started from 1989")
    if r > 31:
        raise ValueError("Heisei era ended at 2019")
    return r


def from_yyyy_to_showa_era(year: int) -> int:
    """convert western year to Japanese Showa era year"""
    r = year - 1925
    if r <= 0:
        raise ValueError("Showa era started from 1926")
    if r > 64:
        raise ValueError("Showa era ended at 1989")
    return r


def from_yyyy_to_reiwa_era(year: int) -> int:
    """convert western year to Japanese Reiwa era year"""
    r = year - 2018
    if r <= 0:
        raise ValueError("Reiwa era started from May 1st, 2019")
    return r

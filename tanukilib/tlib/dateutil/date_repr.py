import datetime

def cur_datetime_as_std_fmt_str(date_delimitor:str = '-',
                                time_delimitor:str = ':',
                                with_t:bool = True,
                                with_tz:bool = False, 
                                with_ssec:bool = False,
                                timezone:datetime.timezone = datetime.timezone.utc) -> str:
    fmt = f"%Y{date_delimitor}%m{date_delimitor}%d"
    if with_t:
        fmt += "T"
    fmt += f"%H{time_delimitor}%M{time_delimitor}%S"
    if with_ssec:
        fmt += ".%f"
    if with_tz:
        fmt += "%z"
    return datetime.datetime.now(timezone).strftime(fmt)

def get_datetime_as_std_fmt_str(year:int,
                                month:int,
                                day:int,
                                hour:int,
                                minute:int,
                                sec:int,
                                date_delimitor:str = '-',
                                time_delimitor:str = ':',
                                with_t:bool = True,
                                with_tz:bool = False,
                                with_ssec:bool = False,
                                timezone:datetime.timezone = datetime.timezone.utc) -> str:
    fmt = f"%Y{date_delimitor}%m{date_delimitor}%d"
    if with_t:
        fmt += "T"
    fmt += f"%H{time_delimitor}%M{time_delimitor}%S"
    if with_ssec:
        fmt += ".%f"
    if with_tz:
        fmt += "%z"
    return datetime.datetime(year, month, day, hour, minute, sec, tzinfo = timezone).strftime(fmt)

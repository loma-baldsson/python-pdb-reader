from datetime import datetime, timedelta

# Jan 1, 1904
PALM_EPOCH = datetime(1904, 1, 1)

UNIX_TIME = 0
PALM_TIME = 1


def detect_timestamp_time(timestamp: int) -> int:
    # get top bit of a 32-bit integer
    # if it's set, it uses palm time
    # if it's clear, it uses unix time
    # fortunately the enum's values account for this
    return timestamp >> (32-1)


def palm_to_datetime(timestamp: int, force_palm_time: bool = False) -> datetime:
    # detects the correct epoch (Palm Epoch or Unix Epoch) and use that
    # according to various sources both are used depending
    # on the os used for creating the .pdb file
    if detect_timestamp_time(timestamp) == PALM_TIME or force_palm_time:
        return PALM_EPOCH + timedelta(seconds=timestamp)
    else:
        return datetime.fromtimestamp(timestamp)


def datetime_to_palm(time: datetime) -> int:
    return int((time - PALM_EPOCH).total_seconds())

# TODO: add tests for detect_timestamp_time() and palm_to_datetime()

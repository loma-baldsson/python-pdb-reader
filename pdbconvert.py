import datetime

# Jan 1, 1904
PALM_EPOCH = datetime.datetime(1904, 1, 1)


def palm_to_datetime(palm_time):
    return PALM_EPOCH + datetime.timedelta(seconds=palm_time)


def datetime_to_palm(time):
    return int((time - PALM_EPOCH).total_seconds())

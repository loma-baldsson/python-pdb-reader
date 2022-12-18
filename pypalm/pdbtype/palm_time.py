from datetime import datetime

from .fixed_size_ints import DWord
from .. import palm_to_datetime, datetime_to_palm


class PalmTime(DWord):
    def get_default(self):
        # just an arbitrary date
        return datetime(2020, 1, 1)

    def getter(self):
        timestamp = super().getter()
        return palm_to_datetime(timestamp)

    def setter(self, value):
        assert isinstance(value, datetime)

        super().setter(datetime_to_palm(value))

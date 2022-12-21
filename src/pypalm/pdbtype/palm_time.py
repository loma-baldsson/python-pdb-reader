from datetime import datetime

from . import DWord
from .. import palm_to_datetime, datetime_to_palm


class PalmTime(DWord):
    def get_default(self) -> datetime:
        # just an arbitrary date
        return datetime(2020, 1, 1)

    def getter(self) -> datetime:
        timestamp = super().getter()
        return palm_to_datetime(timestamp)

    def setter(self, value: datetime) -> None:
        # TODO: Warn user if their is chance of possible internal confusion between palm time and unix time
        assert isinstance(value, datetime)

        super().setter(datetime_to_palm(value))

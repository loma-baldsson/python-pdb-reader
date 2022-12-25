from datetime import datetime

from . import PDBTypeBase
from ..pdbconvert import palm_to_datetime, datetime_to_palm


class PalmTime(PDBTypeBase):
    def __init__(self):
        # palmtime objects are always 4 bytes
        super().__init__(4)

    def get_default(self) -> datetime:
        # just an arbitrary date
        return datetime(2020, 1, 1)

    def getter(self) -> datetime:
        timestamp = int.from_bytes(self._value, "big")
        return palm_to_datetime(timestamp)

    def setter(self, value: datetime) -> None:
        # TODO: Warn user if their is chance of possible internal confusion between palm time and unix time
        timestamp = datetime_to_palm(value)
        self._value = timestamp.to_bytes(self._size, "big")

from . import PDBTypeBase


class BigEndianInt(PDBTypeBase):
    def get_default(self):
        return 0

    def getter(self):
        return int.from_bytes(self._value, "big")

    def setter(self, value):
        # TODO: raise an error if value will overflow
        self._value = value.to_bytes(self._size, "big")

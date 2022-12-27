from . import PDBTypeBase


class BigEndianInt(PDBTypeBase):
    def get_default(self) -> int:
        return 0

    def getter(self) -> int:
        return int.from_bytes(self._value, "big")

    def setter(self, value: int) -> None:
        # TODO: raise an error if value will overflow
        self._value = value.to_bytes(self._size, "big")

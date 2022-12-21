from . import PDBTypeBase


class FixedLengthString(PDBTypeBase):
    def get_default(self) -> str:
        return " " * self._size

    def getter(self) -> str:
        return self._value.decode("ascii")

    def setter(self, value: str) -> None:
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"
        assert value.isascii(), "Value isn't ascii"

        self._value = value.encode("ascii")

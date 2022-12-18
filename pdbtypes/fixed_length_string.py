from .pdb_type_base import PDBTypeBase


class FixedLengthString(PDBTypeBase):
    def get_default(self):
        return " " * self._size

    def getter(self):
        return self._value.decode("ascii")

    def setter(self, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"
        assert value.isascii(), "Value isn't ascii"

        self._value = value.encode("ascii")

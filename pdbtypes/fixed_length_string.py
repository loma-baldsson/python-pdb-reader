from .pdb_type_base import PDBTypeBase, PDBTypeBaseBytes


class FixedLengthString(PDBTypeBase):
    def getter(self, value):
        return value.decode("ascii")

    def setter(self, old_value, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) == self._length, f"Value isn't the correct length ({self._length})"
        assert value.isascii(), "Value isn't ascii"

        return value.encode("ascii")


class FixedLengthStringBytes(PDBTypeBaseBytes):
    pass

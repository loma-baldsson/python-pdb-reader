class PDBTypeBase:
    def __init__(self, length):
        self._length = length

    def getter(self, value):
        raise AttributeError(f"No getter for attribute of type {type(self).__name__}")

    def setter(self, old_value, value):
        raise AttributeError(f"No setter for attribute of type {type(self).__name__}")

    def deleter(self, value):
        raise AttributeError(f"No deleter for attribute of type {type(self).__name__}")


class PDBTypeBaseBytes(PDBTypeBase):
    def getter(self, value):
        return value

    def setter(self, old_value, value):
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._length, f"Value isn't the correct length ({self._length})"

        return value

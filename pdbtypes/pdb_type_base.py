class PDBTypeBase:
    def __init__(self, size):
        self._size = size

    def get_default(self):
        raise AttributeError(f"No default value for type {type(self).__name__}")

    def getter(self, value):
        raise AttributeError(f"No getter for attribute of type {type(self).__name__}")

    def setter(self, old_value, value):
        raise AttributeError(f"No setter for attribute of type {type(self).__name__}")

    def deleter(self, value):
        raise AttributeError(f"No deleter for attribute of type {type(self).__name__}")


class PDBTypeBaseBytes(PDBTypeBase):
    def get_default(self):
        return b"\0" * self._size

    def getter(self, value):
        return value

    def setter(self, old_value, value):
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"

        return value

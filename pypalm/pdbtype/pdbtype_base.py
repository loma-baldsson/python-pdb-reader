class PDBTypeBase:
    def __init__(self, size):
        self._size = size
        self.setter(self.get_default())

    def get_default(self):
        raise AttributeError(f"No default value for type {type(self).__name__}")

    def getter(self):
        raise AttributeError(f"No getter for attribute of type {type(self).__name__}")

    def setter(self, value):
        raise AttributeError(f"No setter for attribute of type {type(self).__name__}")

    def getter_bytes(self):
        return self._value

    def setter_bytes(self, value):
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"

        self._value = value

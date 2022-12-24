from typing import Any


class PDBTypeBase:
    def __init__(self, size: int, value: Any = None):
        self._size: int = size
        self._value: bytes

        if value:
            self.setter(value)
        else:
            self.setter(self.get_default())

    def __eq__(self, other):
        # directly compare the underlying byte objects
        # this handles edge cases where comparing two different types might result in true being returned
        return self._value == other._value

    def __repr__(self):
        return f"{type(self).__name__}({self.getter()!r})"

    def get_default(self) -> Any:
        raise AttributeError(f"No default value for type {type(self).__name__}")

    def getter(self) -> Any:
        raise AttributeError(f"No getter for attribute of type {type(self).__name__}")

    def setter(self, value: Any) -> None:
        raise AttributeError(f"No setter for attribute of type {type(self).__name__}")

    def getter_bytes(self) -> bytes:
        return self._value

    def setter_bytes(self, value: bytes) -> None:
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"

        self._value = value

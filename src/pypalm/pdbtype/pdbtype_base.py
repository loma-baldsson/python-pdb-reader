from typing import Any


class PDBTypeBase:
    def __init__(self, size: int, value: Any = None):
        self._size: int = size
        self._value: bytes

        if value:
            self.setter(value)
        else:
            self.setter(self.get_default())

    def __lt__(self, other):
        return self.getter() < other.getter()

    def __le__(self, other):
        return self.getter() <= other.getter()

    def __eq__(self, other):
        return self.getter() == other.getter()

    def __ne__(self, other):
        return self.getter() != other.getter()

    def __gt__(self, other):
        return self.getter() > other.getter()

    def __ge__(self, other):
        return self.getter() >= other.getter()

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

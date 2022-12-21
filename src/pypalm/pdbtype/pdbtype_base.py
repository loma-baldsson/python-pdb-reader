from typing import Any


class PDBTypeBase:
    def __init__(self, size: int):
        self._size: int = size
        self._value: bytes
        self.setter(self.get_default())

    def get_default(self) -> Any:
        raise AttributeError(f"No default value for type {type(self).__name__}")

    def getter(self) -> Any:
        raise AttributeError(f"No getter for attribute of type {type(self).__name__}")

    def setter(self, value: Any) -> None:
        raise AttributeError(f"No setter for attribute of type {type(self).__name__}")

    def getter_bytes(self) -> bytes:
        return self._value

    def setter_bytes(self, value: bytes) -> None:
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._size, f"Value isn't the correct length ({self._size})"

        self._value = value

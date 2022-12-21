from . import FixedLengthString


class NullTerminatedString(FixedLengthString):
    def get_default(self) -> str:
        return ""

    def getter(self) -> str:
        decoded_value = super().getter()
        return decoded_value.split("\0")[0]

    def setter(self, value: str) -> None:
        assert len(value) < self._size, f"Length is over maximum ({self._size})"
        assert value.isascii(), "Value isn't ascii"
        assert value.find("\0") == -1, r"Early null char ('\0') was found"

        self._value = value.ljust(self._size, "\0").encode("ascii")

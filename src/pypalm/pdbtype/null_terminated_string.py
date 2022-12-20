from . import FixedLengthString


class NullTerminatedString(FixedLengthString):
    def get_default(self):
        return ""

    def getter(self):
        decoded_value = super().getter()
        return decoded_value.split("\0")[0]

    def setter(self, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) < self._size, f"Length is over maximum ({self._size})"
        assert value.isascii(), "Value isn't ascii"
        assert value.find("\0") == -1, r"Early null char ('\0') was found"

        self._value = value.ljust(self._size, "\0").encode("ascii")
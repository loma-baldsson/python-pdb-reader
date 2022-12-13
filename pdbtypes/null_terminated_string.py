from .fixed_length_string import FixedLengthString, FixedLengthStringBytes


class NullTerminatedString(FixedLengthString):
    def get_default(self):
        return ""

    def getter(self, value):
        decoded_value = super().getter(value)
        return decoded_value.split("\0")[0]

    def setter(self, old_value, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) < self._size, f"Length is over maximum ({self._size})"
        assert value.isascii(), "Value isn't ascii"
        assert value.find("\0") == -1, r"Early null char ('\0') was found"

        return value.ljust(32, "\0").encode("ascii")


class NullTerminatedStringBytes(FixedLengthStringBytes):
    pass

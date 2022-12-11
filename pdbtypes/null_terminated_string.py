class NullTerminatedString:
    def __init__(self, attrs_dict, attr_name, max_length):
        self._attrs_dict = attrs_dict
        self._attr_name = attr_name
        self._length = max_length

    def __get__(self, instance, owner=None):
        str_value = self._attrs_dict[self._attr_name].decode("ascii")
        return str_value

    def __set__(self, instance, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) < self._length, f"Length is over maximum ({self._length})"
        assert value.find("\0") == -1, "Null terminator in string"
        assert value.isascii(), "Value isn't ascii"

        byte_val = value.ljust(32, "\0").encode("ascii")
        self._attrs_dict[self._attr_name] = byte_val

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


class NullTerminatedStringBytes(NullTerminatedString):
    def __get__(self, instance, owner=None):
        return self._attrs_dict[self._attr_name]

    def __set__(self, instance, value):
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._length, f"Value isn't the correct length ({self._length})"

        self._attrs_dict[self._attr_name] = value

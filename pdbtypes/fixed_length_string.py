class FixedLengthString:
    def __init__(self, attr_name, length, docs=""):
        self._attr_name = attr_name
        self._length = length
        self.__docs__ = docs

    def __get__(self, instance, owner=None):
        str_value = getattr(instance, self._attr_name).decode("ascii")
        return str_value

    def __set__(self, instance, value):
        assert isinstance(value, str), "Value isn't a string"
        assert len(value) == self._length, f"Value isn't the correct length ({self._length})"
        assert value.isascii(), "Value isn't ascii"

        byte_val = value.encode("ascii")
        setattr(instance, self._attr_name, byte_val)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


class FixedLengthStringBytes(FixedLengthString):
    def __get__(self, instance, owner=None):
        return getattr(instance, self._attr_name)

    def __set__(self, instance, value):
        assert isinstance(value, bytes), "Value isn't a byte sequence"
        assert len(value) == self._length, f"Value isn't the correct length ({self._length})"

        setattr(instance, self._attr_name, value)

from datetime import datetime
from typing import Any

import pytest

from pypalm.pdbtype import PDBTypeBase, BigEndianInt, PalmTime, FixedLengthString, NullTerminatedString


class ExamplePDBType(PDBTypeBase):
    def __init__(self, value: Any = None):
        super().__init__(1, value)

    def get_default(self) -> bool:
        return False

    def getter(self) -> bool:
        return bool.from_bytes(self._value, "big")

    def setter(self, value: bool) -> None:
        self._value = value.to_bytes(1, "big")


class TestPDBType:
    def test_set_default(self):
        obj = ExamplePDBType()
        assert obj._value == bytes.fromhex("00")

    def test_init_default(self):
        obj = ExamplePDBType(True)
        assert obj._value == bytes.fromhex("01")

    def test_getter(self):
        # Usually you should do something like "assert x" instead of "assert x == True"
        # However, I'm ignoring this convention because obj.getter() returns a boolean value, and it's not intended
        # to be used as a condition

        obj = ExamplePDBType()
        assert obj.getter() == False

        obj._value = bytes.fromhex("01")
        assert obj.getter() == True

    def test_setter(self):
        obj = ExamplePDBType()

        obj.setter(True)
        assert obj._value == bytes.fromhex("01")

        obj.setter(False)
        assert obj._value == bytes.fromhex("00")


class TestBigEndianInt:
    def test_getter(self):
        obj = BigEndianInt(4)
        obj._value = bytes.fromhex("00 00 04 d2")

        assert obj.getter() == 1234

    def test_setter(self):
        obj = BigEndianInt(4)
        obj.setter(1234)

        assert obj._value == bytes.fromhex("00 00 04 d2")


class TestPalmTime:
    def test_getter(self):
        obj = PalmTime()
        obj._value = bytes.fromhex("DF CA A0 00")

        assert obj.getter() == datetime(2022, 12, 23)

    def test_setter(self):
        obj = PalmTime()
        obj.setter(datetime(2022, 12, 23))

        assert obj._value == bytes.fromhex("DF CA A0 00")


class TestFixedLengthString:
    def test_getter(self):
        obj = FixedLengthString(4)
        obj._value = bytes.fromhex("74 65 73 74")

        assert obj.getter() == "test"

    def test_setter(self):
        obj = FixedLengthString(4)
        obj.setter("test")

        assert obj._value == bytes.fromhex("74 65 73 74")

    @pytest.mark.parametrize("size,value", [(4, "wow"), (4, "hello")])
    def test_set_incorrect_length(self, size, value):
        obj = FixedLengthString(size)

        with pytest.raises(AssertionError):
            obj.setter(value)

    def test_set_not_ascii(self):
        obj = FixedLengthString(4)

        with pytest.raises(AssertionError):
            # nerd emoji
            obj.setter(bytes.fromhex("F0 9F A4 93").decode("utf-8"))


class TestNullTerminatedString:
    def test_getter(self):
        obj = NullTerminatedString(8)
        obj._value = bytes.fromhex("74 65 73 74 00 00 00 00")

        assert obj.getter() == "test"

    def test_setter(self):
        obj = NullTerminatedString(8)
        obj.setter("test")

        assert obj._value == bytes.fromhex("74 65 73 74 00 00 00 00")

    @pytest.mark.parametrize("size,value", [(4, "test"), (4, "hello")])
    def test_set_incorrect_length(self, size, value):
        obj = NullTerminatedString(size)

        with pytest.raises(AssertionError):
            obj.setter(value)

    def test_set_not_ascii(self):
        obj = NullTerminatedString(8)

        with pytest.raises(AssertionError):
            # nerd emoji
            obj.setter(bytes.fromhex("F0 9F A4 93").decode("utf-8"))

    @pytest.mark.parametrize("size,value", [(8, "hello\0"), (16, "test\0test")])
    def test_set_early_null_char(self, size, value):
        obj = NullTerminatedString(size)

        with pytest.raises(AssertionError):
            obj.setter(value)

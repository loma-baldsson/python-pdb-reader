from typing import Any

from . import BigEndianInt


class Byte(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(1, value)

    def __repr__(self):
        return f"{type(self).__name__}({self.getter()!r})"


class Word(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(2, value)

    def __repr__(self):
        return f"{type(self).__name__}({self.getter()!r})"


class DWord(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(4, value)

    def __repr__(self):
        return f"{type(self).__name__}({self.getter()!r})"

# TODO: somehow get rid of the code repetition in __repr__()

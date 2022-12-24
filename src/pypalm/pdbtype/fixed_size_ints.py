from typing import Any

from . import BigEndianInt


class Byte(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(1, value)


class Word(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(2, value)


class DWord(BigEndianInt):
    def __init__(self, value: Any = None):
        super().__init__(4, value)

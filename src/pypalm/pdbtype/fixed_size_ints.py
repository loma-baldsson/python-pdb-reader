from . import BigEndianInt


class Byte(BigEndianInt):
    def __init__(self):
        super().__init__(1)


class Word(BigEndianInt):
    def __init__(self):
        super().__init__(2)


class DWord(BigEndianInt):
    def __init__(self):
        super().__init__(4)

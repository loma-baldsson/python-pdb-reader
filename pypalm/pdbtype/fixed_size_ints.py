from .big_endian_int import BigEndianInt


class Byte(BigEndianInt):
    def __init__(self, *args):
        super().__init__(1, *args)


class Word(BigEndianInt):
    def __init__(self, *args):
        super().__init__(2, *args)


class DWord(BigEndianInt):
    def __init__(self, *args):
        super().__init__(4, *args)

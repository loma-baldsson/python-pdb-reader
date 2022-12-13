from .big_endian_int import BigEndianInt, BigEndianIntBytes


class Byte(BigEndianInt):
    def __init__(self, *args):
        super().__init__(1, *args)


class ByteBytes(BigEndianIntBytes):
    def __init__(self, *args):
        super().__init__(1, *args)


class Word(BigEndianInt):
    def __init__(self, *args):
        super().__init__(2, *args)


class WordBytes(BigEndianIntBytes):
    def __init__(self, *args):
        super().__init__(2, *args)


class DWord(BigEndianInt):
    def __init__(self, *args):
        super().__init__(4, *args)


class DWordBytes(BigEndianIntBytes):
    def __init__(self, *args):
        super().__init__(4, *args)

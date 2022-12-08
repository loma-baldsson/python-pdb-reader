class PDBReadError(Exception):
    pass


def _get_int(file, length):
    return int.from_bytes(file.read(length), "big")


def get_byte(file):
    return _get_int(file, 1)


def get_word(file):
    return _get_int(file, 2)


def get_dword(file):
    return _get_int(file, 4)


def get_string(file, length, has_terminator=False):
    s = file.read(length).decode("ascii")
    if has_terminator:
        return s.split("\0")[0]

    return s
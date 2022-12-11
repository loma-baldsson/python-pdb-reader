class PDBWriteError(Exception):
    pass


def put_int(file, val, length):
    return file.write(val.to_bytes(length, "big"))


def put_byte(file, val):
    return put_int(file, val, 1)


def put_word(file, val):
    return put_int(file, val, 2)


def put_dword(file, val):
    return put_int(file, val, 4)


def put_string(file, val, length, requires_terminator=False):
    if len(val) > length-1 and requires_terminator:
        raise PDBWriteError()

    return file.write(val.ljust(length, "\0").encode("ascii"))
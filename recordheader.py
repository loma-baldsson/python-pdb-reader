from pdbread import get_byte, get_dword, get_int
from pdbwrite import put_byte, put_dword, put_int


class RecordHeader:
    def __init__(self):
        self.offset = 0
        self.attributes = 0
        self.unique_id = 0

    @classmethod
    def load_from_file(cls, file):
        self = cls()

        self.offset = get_dword(file)
        self.attributes = get_byte(file)
        self.unique_id = get_int(file, 3)

        return self

    def write_to_file(self, file):
        put_dword(file, self.offset)
        put_byte(file, self.attributes)
        put_int(file, self.unique_id, 3)

    def __str__(self):
        out = f"offset: {self.offset!r}\n"
        out += f"attributes: {self.attributes!r}\n"
        out += f"unique_id: {self.unique_id!r}\n"

        return out

# TODO: Make getter/setter methods for each attribute

from .. import NullTerminatedString, FixedLengthString, Word, DWord, PalmTime, Template


class PDBHeader(Template):
    def __init__(self):
        self._items = {
            "name": NullTerminatedString(32),
            "attributes": Word(),
            "version": Word(),
            "creation_time": PalmTime(),
            "modification_time": PalmTime(),
            "backup_time": PalmTime(),
            "modification_number": DWord(),
            "app_info_offset": DWord(),
            "sort_info_offset": DWord(),
            "type": FixedLengthString(4),
            "creator": FixedLengthString(4),
            "unique_id": DWord(),
            "next_record_id": DWord(),
            "num_records": Word(),
        }

    @classmethod
    def load_from_file(cls, file):
        self = cls()

        for item in self._items.values():
            item_size = len(item.getter_bytes())
            item.setter_bytes(file.read(item_size))

        return self

    def write_to_file(self, file):
        for item in self._items.values():
            file.write(item.getter_bytes())

    def __str__(self):
        out = ""

        for key, item in self._items.items():
            val = item.getter()
            out += f"{key}: {val!r}\n"

        return out

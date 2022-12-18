from .. import BigEndianInt, Byte, DWord, template_wrapper


@template_wrapper
class RecordHeader:
    def __init__(self):
        self._items = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

    @classmethod
    def load_from_file(cls, file):
        self = cls()

        for key, item in self._items.items():
            print(key)
            item_size = len(item.getter_bytes())
            print(item_size)
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

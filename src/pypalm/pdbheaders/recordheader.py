from .. import BigEndianInt, Byte, DWord, FileLoadedTemplate


class RecordHeader(FileLoadedTemplate):
    def __init__(self, **kwargs):
        super().__init__()
        self._items = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

        self.load_values(**kwargs)

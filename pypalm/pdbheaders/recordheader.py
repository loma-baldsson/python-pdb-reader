from .. import BigEndianInt, Byte, DWord, FileLoadedTemplate


class RecordHeader(FileLoadedTemplate):
    def __init__(self):
        self._items = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

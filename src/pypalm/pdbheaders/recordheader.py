from .. import BigEndianInt, Byte, DWord, FileLoadedTemplate


class RecordHeader(FileLoadedTemplate):
    def __init__(self, **kwargs):
        items = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

        super().__init__(items, **kwargs)
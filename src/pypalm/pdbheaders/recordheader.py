from typing import Any

from .. import BigEndianInt, Byte, DWord, FileLoadedTemplate, PDBTypeBase


class RecordHeader(FileLoadedTemplate):
    def __init__(self, **kwargs: Any):
        super().__init__()
        self._items: dict[str, PDBTypeBase] = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

        self.load_values(**kwargs)

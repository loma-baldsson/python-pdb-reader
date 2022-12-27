from typing import Any

from ..pdbtype import PDBTypeBase, BigEndianInt, Byte, DWord
from ..pdbtemplates import FileLoadedTemplate

class RecordHeader(FileLoadedTemplate):
    def __init__(self, **kwargs: Any):
        super().__init__()
        self._items: dict[str, PDBTypeBase] = {
            "offset": DWord(),
            "attributes": Byte(),
            "unique_id": BigEndianInt(3),
        }

        self.load_values(**kwargs)

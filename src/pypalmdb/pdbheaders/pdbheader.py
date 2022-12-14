from typing import Any

from ..pdbtype import PDBTypeBase, FixedLengthString, NullTerminatedString, Word, DWord, PalmTime
from ..pdbtemplates import FileLoadedTemplate


class PDBHeader(FileLoadedTemplate):
    def __init__(self, **kwargs: Any):
        super().__init__()
        self._items: dict[str, PDBTypeBase] = {
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

        self.load_values(**kwargs)

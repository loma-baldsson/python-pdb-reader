from typing import BinaryIO

from typing_extensions import Self

from . import Template


class FileLoadedTemplate(Template):
    @classmethod
    def load_from_file(cls, file: BinaryIO) -> Self:
        self = cls()

        for key, item in self._items.items():
            item_size = len(item.getter_bytes())
            item.setter_bytes(file.read(item_size))

        return self

    def write_to_file(self, file: BinaryIO) -> None:
        for item in self._items.values():
            file.write(item.getter_bytes())

from typing import Any, Iterable

from ..pdbtype import PDBTypeBase

BYTES_SUFFIX = "_bytes"


class Template:
    def __init__(self):
        self._items: dict[str, PDBTypeBase]

    def __getattr__(self, item: str) -> Any:
        if not Template.has_initialized(self):
            return object.__getattribute__(self, item)

        items = self._items

        if item in items:
            return items[item].getter()
        elif item.endswith(BYTES_SUFFIX):
            item = item[:-len(BYTES_SUFFIX)]
            if item in items:
                return items[item].getter_bytes()
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key: str, value: Any) -> None:
        if not Template.has_initialized(self):
            object.__setattr__(self, key, value)
            return

        items = self._items

        if key in items:
            items[key].setter(value)
        elif key.endswith(BYTES_SUFFIX):
            key = key[:-len(BYTES_SUFFIX)]
            if key in items:
                items[key].setter_bytes(value)
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item: str) -> None:
        if not Template.has_initialized(self):
            object.__delattr__(self, item)
            return

        items = self._items

        if (item in items
                or (item.endswith(BYTES_SUFFIX) and item[:-len(BYTES_SUFFIX)] in items)):
            raise AttributeError(f"'{type(self).__name__}' object attribute '{item}' is read-only")
        else:
            object.__delattr__(self, item)

    def __dir__(self) -> Iterable[str]:
        if not Template.has_initialized(self):
            return object.__dir__(self)

        return list(object.__dir__(self)) + list(self._items.keys())

    def __repr__(self) -> str:
        out_kwargs = []
        for key, item in self._items.items():
            if item.getter() != item.get_default():
                out_kwargs.append(f"{key}={item.getter()!r}")

        return f"{type(self).__name__}({', '.join(out_kwargs)})"

    def __str__(self) -> str:
        out = ""

        for key, item in self._items.items():
            val = item.getter()
            out += f"{key}: {val!r}\n"

        return out

    def __eq__(self, other):
        return self._items == other._items

    def load_values(self, **kwargs):
        for key, value in kwargs.items():
            if key in self._items:
                self._items[key].setter(value)
            else:
                raise AttributeError(f"Object of type '{type(self).__name__}' has no attribute '{key}'")

    def has_initialized(self) -> bool:
        try:
            _ = object.__getattribute__(self, "_items")
        except AttributeError:
            return False
        else:
            return True

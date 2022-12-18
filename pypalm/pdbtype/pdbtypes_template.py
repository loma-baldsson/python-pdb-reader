BYTES_SUFFIX = "_bytes"


class Template:
    def __getattr__(self, item):
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

    def __setattr__(self, key, value):
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

    def __delattr__(self, item):
        if not Template.has_initialized(self):
            object.__delattr__(self, item)
            return

        items = self._items

        if (item in items
                or (item.endswith(BYTES_SUFFIX) and item[:-len(BYTES_SUFFIX)] in items)):
            raise AttributeError(f"'{type(self).__name__}' object attribute '{item}' is read-only")
        else:
            object.__delattr__(self, item)

    def __dir__(self):
        if not Template.has_initialized(self):
            return object.__dir__(self)

        return list(object.__dir__(self)) + list(self._items.keys())

    def __str__(self):
        out = ""

        for key, item in self._items.items():
            val = item.getter()
            out += f"{key}: {val!r}\n"

        return out

    def has_initialized(self):
        try:
            _ = object.__getattribute__(self, "_items")
        except AttributeError:
            return False
        else:
            return True


class FileLoadedTemplate(Template):
    @classmethod
    def load_from_file(cls, file):
        self = cls()

        for key, item in self._items.items():
            item_size = len(item.getter_bytes())
            item.setter_bytes(file.read(item_size))

        return self

    def write_to_file(self, file):
        for item in self._items.values():
            file.write(item.getter_bytes())

from .pdb_type_base import PDBTypeBase, PDBTypeBaseBytes


class BigEndianInt(PDBTypeBase):
    def get_default(self):
        return 0

    def getter(self, value):
        return int.from_bytes(value, "big")

    def setter(self, old_value, value):
        # TODO: raise an error if value will overflow
        return value.to_bytes(self._size, "big")


class BigEndianIntBytes(PDBTypeBaseBytes):
    pass

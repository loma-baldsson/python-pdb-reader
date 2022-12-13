def pdbtype(*args):
    def wrapper(doc):
        return PDBType(doc, *args)

    return wrapper


class PDBType:
    def __init__(self, doc, type_instance, attr_name):
        self.__doc__ = doc.__doc__
        self._type_instance = type_instance
        self._attr_name = attr_name

    def __get__(self, instance, owner=None):
        if self._attr_name in dir(instance):
            value = getattr(instance, self._attr_name)
            return self._type_instance.getter(value)

        return self._type_instance.get_default()

    def __set__(self, instance, value):
        old_value = getattr(instance, self._attr_name)
        setattr(instance, self._attr_name, self._type_instance.setter(old_value, value))

    def __delete__(self, instance):
        value = getattr(instance, self._attr_name)

        self._type_instance.deleter(value)
        delattr(instance, self._attr_name)

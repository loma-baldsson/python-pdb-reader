def doc(cls, *args):
    def wrapper(func):
        return cls(*args, func.__doc__)

    return wrapper

def doc(func, cls, *args):
    return cls(*args, func.__doc__)

class Test:
    def __init__(self):
        print("__init__() called!")

    def __get__(self, instance, owner=None):
        print(f"__get__() called with {instance=} and {owner=}!")

    def __set__(self, instance, value):
        print(f"__set__() called with {instance=} and {value=}!")

    def __delete__(self, instance):
        print(f"__delete__() called with {instance=}!")


class MyObject:
    test = Test()


def main():
    my_obj = MyObject()
    my_obj.test
    my_obj.test = 5
    del my_obj.test

if __name__ == "__main__":
    main()

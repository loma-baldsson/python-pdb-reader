import datetime

from pypalm import FixedLengthString, NullTerminatedString, BigEndianInt, template_wrapper, PalmTime


@template_wrapper
class Test:
    def __init__(self):
        self._items = {
            "x": FixedLengthString(16),
            "y": NullTerminatedString(16),
            "z": BigEndianInt(2),
            "date": PalmTime()
        }


def main():
    test = Test()

    print(test.x)
    print(test.x_bytes.hex(" "))
    test.x = "HelloHelloHelloH"
    print(test.x)
    print(test.x_bytes.hex(" "))

    print(test.y)
    test.y = "Hello, World!"
    print(test.y)
    print(len(test.y_bytes))

    test.z = 20
    print(test.z)
    print(test.z_bytes)

    print(test.date)
    test.date = datetime.datetime.now()
    print(test.date)    # filename = sys.argv[1] if len(sys.argv) > 1 else "./test/test.pdb"
    # with open(filename, "rb") as f:
    #     header = PDBHeader.load_from_file(f)
    #
    # print(header)

    # with open(filename, "wb") as f:
    #     header.name = "edited"
    #     header.write_to_file(f)


if __name__ == "__main__":
    main()

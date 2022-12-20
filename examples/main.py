import datetime
import sys
from os import path

from pypalm import FixedLengthString, NullTerminatedString, BigEndianInt, PalmTime
from pypalm import PDBHeader, RecordHeader
from pypalm import Template


class Test(Template):
    def __init__(self, **kwargs):
        self._items = {
            "x": FixedLengthString(16),
            "y": NullTerminatedString(16),
            "z": BigEndianInt(2),
            "date": PalmTime()
        }

        super().__init__(**kwargs)


def test_template():
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
    print(test.date)


def main():
    # taken from https://stackoverflow.com/a/4381638
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "pdbs", "test.pdb"))

    filename = sys.argv[1] if len(sys.argv) > 1 else filepath
    with open(filename, "rb") as f:
        header = PDBHeader.load_from_file(f)

        record_headers = []
        for i in range(header.num_records):
            record_headers.append(RecordHeader.load_from_file(f))

    new_header = PDBHeader(name="Hello")

    print(new_header)
    print(repr(header), "\n")
    print(record_headers)


if __name__ == "__main__":
    main()

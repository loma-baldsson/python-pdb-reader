import sys

from pypalm.pdbtype import FixedLengthString, NullTerminatedString, BigEndianInt, PalmTime, Template
from pypalm.pdbheaders import PDBHeader, RecordHeader


class Test(Template):
    def __init__(self):
        self._items = {
            "x": FixedLengthString(16),
            "y": NullTerminatedString(16),
            "z": BigEndianInt(2),
            "date": PalmTime()
        }


def main():
    # test = Test()
    #
    # print(test.x)
    # print(test.x_bytes.hex(" "))
    # test.x = "HelloHelloHelloH"
    # print(test.x)
    # print(test.x_bytes.hex(" "))
    #
    # print(test.y)
    # test.y = "Hello, World!"
    # print(test.y)
    # print(len(test.y_bytes))
    #
    # test.z = 20
    # print(test.z)
    # print(test.z_bytes)
    #
    # print(test.date)
    # test.date = datetime.datetime.now()
    # print(test.date)

    filename = sys.argv[1] if len(sys.argv) > 1 else "./test/test.pdb"
    with open(filename, "rb") as f:
        header = PDBHeader.load_from_file(f)

    record_headers = []
    for i in range(header.num_records):
        record_headers.append(RecordHeader.load_from_file(f))

    print(header)
    print(record_headers)


if __name__ == "__main__":
    main()

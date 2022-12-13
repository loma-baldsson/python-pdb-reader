import datetime
import sys
import pprint

from pdbheader import PDBHeader
from pdbconvert import palm_to_datetime, datetime_to_palm
from pdbtypes import pdbtype, FixedLengthString
from pypalm.pdbtypes import FixedLengthStringBytes


class Test:
    def __init__(self):
        self._x = b""

    @pdbtype(FixedLengthString(5), "_x")
    def x(self):
        """Hello"""

    @pdbtype(FixedLengthStringBytes(5), "_x")
    def x_bytes(self):
        """Bytes of x"""


def main():
    test = Test()
    print(test.x)
    test.x = "Hello"
    print(test.x)
    print(test.x_bytes)
    # filename = sys.argv[1] if len(sys.argv) > 1 else "./test/test.pdb"
    # with open(filename, "rb") as f:
    #     header = PDBHeader.load_from_file(f)
    #
    # print(header)

    # with open(filename, "wb") as f:
    #     header.name = "edited"
    #     header.write_to_file(f)


if __name__ == "__main__":
    main()

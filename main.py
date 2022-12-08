import datetime
import sys
import pprint

from pdbheader import PDBHeader
from pdbconvert import palm_to_datetime, datetime_to_palm


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "./test/test.pdb"
    with open(filename, "rb") as f:
        header = PDBHeader.load_from_file(f)

    print(header)

    # with open(filename, "wb") as f:
    #     header.name = "edited"
    #     header.write_to_file(f)


if __name__ == "__main__":
    main()

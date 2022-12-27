import sys
from os import path

from pypalmdb.pdbheaders import PDBHeader, RecordHeader


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

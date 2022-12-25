from datetime import datetime
from hashlib import sha256

from pypalm.pdbheaders import PDBHeader
from .test_files import tmp_files

SAMPLE_TIME = datetime(2022, 12, 23)
SAMPLE_HEADER = PDBHeader(name="test file",
                          version=1,
                          creation_time=SAMPLE_TIME,
                          modification_time=SAMPLE_TIME,
                          type="test",
                          creator="test")

HEADER_CHECKSUM = "e4c1a336e2866bdadb6a7e212ebe03326855eef12cbf9bf796a8cfb890917c19"


class TestPDBHeader:
    def test_read_file(self, tmp_files):
        with open(tmp_files / "test_header.pdb", "rb") as f:
            header = PDBHeader.load_from_file(f)

        assert header == SAMPLE_HEADER

    def test_write_file(self, tmp_path):
        # write the header to a temporary file
        test_path = tmp_path / "test_header.pdb"
        with open(test_path, "wb") as f:
            SAMPLE_HEADER.write_to_file(f)

        # then read from the same file, hash it, and compare it to a hard-coded hash
        with open(test_path, "rb") as f:
            file_contents = f.read()

        file_hash = sha256(file_contents).hexdigest()
        assert file_hash == HEADER_CHECKSUM


class TestRecordHeader:
    # TODO: implement these tests later
    # record reading/writing logic has not been implemented yet
    pass


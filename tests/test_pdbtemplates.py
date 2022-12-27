from hashlib import sha256

import pytest

from pypalmdb.pdbtemplates import Template, FileLoadedTemplate
from pypalmdb.pdbtype import DWord
from .test_files import tmp_files

class ExampleHeader(Template):
    def __init__(self, **kwargs):
        super().__init__()
        self._items = {
            "x": DWord(),
            "y": DWord()
        }

        super().load_values(**kwargs)


class ExampleFileLoadedHeader(FileLoadedTemplate):
    def __init__(self, **kwargs):
        super().__init__()
        self._items = {
            "x": DWord(),
            "y": DWord()
        }
        super().load_values(**kwargs)


SAMPLE_HEADER = ExampleFileLoadedHeader(x=1234, y=5678)
HEADER_CHECKSUM = "ac928ac1ad9e3e6d879668af852975337a7e62fe9543ca499777f8511e2dea8e"


class TestTemplate:
    def test_equality(self):
        header_1 = ExampleHeader()
        header_1.x = 123

        header_2 = ExampleHeader()
        header_2.x = 123

        assert header_1 == header_2

    def test_inequality(self):
        header_1 = ExampleHeader()
        header_1.x = 123

        header_2 = ExampleHeader()
        header_2.x = 321

        assert header_1 != header_2

    def test_init_value(self):
        header = ExampleHeader(x=123)

        assert header.x == 123

    def test_del_value(self):
        header = ExampleHeader(x=123)

        with pytest.raises(AttributeError):
            del header.x


class TestFileLoadedTemplate:
    def test_read_header(self, tmp_files):
        with open(tmp_files / "test_file_loaded_header.bin", "rb") as f:
            header = ExampleFileLoadedHeader.load_from_file(f)

        assert header == SAMPLE_HEADER

    def test_write_file(self, tmp_path):
        # write the header to a temporary file
        test_path = tmp_path / "test_file_loaded_header.bin"
        with open(test_path, "wb") as f:
            SAMPLE_HEADER.write_to_file(f)

        # then read from the same file, hash it, and compare it to a hard-coded hash
        with open(test_path, "rb") as f:
            file_contents = f.read()

        file_hash = sha256(file_contents).hexdigest()
        assert file_hash == HEADER_CHECKSUM

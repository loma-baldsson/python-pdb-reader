import shutil
from pathlib import Path

import pytest

@pytest.fixture
def tmp_files(tmpdir):
    # taken from https://stackoverflow.com/questions/3430395 and https://stackoverflow.com/questions/29631801
    curr_dir = Path(__file__).parent
    test_files = (curr_dir / "test_files").resolve()

    shutil.copytree(test_files, tmpdir, dirs_exist_ok=True)

    return tmpdir

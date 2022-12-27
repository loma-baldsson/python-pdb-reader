from datetime import datetime

import pytest

from pypalmdb.pdbconvert import palm_to_datetime, datetime_to_palm


class TestPDBConvert:
    @pytest.mark.parametrize("timestamp,expected", [(0, datetime(1904, 1, 1)),
                                                    (3029529600, datetime(2000, 1, 1))])
    def test_palm_to_datetime(self, timestamp: int, expected: datetime):
        assert palm_to_datetime(timestamp, True) == expected

    @pytest.mark.parametrize("timestamp,expected", [(946713600, datetime(2000, 1, 1)),
                                                    (3029529600, datetime(2000, 1, 1))])
    def test_palm_to_datetime_detection(self, timestamp: int, expected: datetime):
        assert palm_to_datetime(timestamp) == expected

    @pytest.mark.parametrize("time,expected", [(datetime(1904, 1, 1), 0),
                                               (datetime(2000, 1, 1), 3029529600)])
    def test_datetime_to_palm(self, time: datetime, expected: int):
        assert datetime_to_palm(time) == expected

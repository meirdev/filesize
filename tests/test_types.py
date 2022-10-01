import pytest

from filesize.types import uint


def test_unsigned_int():
    assert uint(1050) == 1050

    with pytest.raises(ValueError):
        uint(-4700)

    assert isinstance(uint(400), int)

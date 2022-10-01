import os
import tempfile
from unittest.mock import patch

import pytest

# name: size
files = {
    "/huge/file/1": 0x0000111122223333,
    "/huge/file/2": 0x11112222FFFFFFFF,
    "/small/file": 0x12345,
}


@pytest.fixture
def ctypes():
    with (
        patch("ctypes.windll", create=True) as windll,
        patch("ctypes.byref") as byref,
    ):
        byref.side_effect = lambda obj: obj

        def GetCompressedFileSizeW(path, high):
            if path in files:
                size = files[path]
                error = 0
            else:
                size = None
                error = 1

            windll.kernel32.GetLastError = error

            if size is None:
                return -1

            high.value = (size & 0xFFFFFFFF00000000) >> 32
            return size & 0x00000000FFFFFFFF

        windll.kernel32.GetCompressedFileSizeW = GetCompressedFileSizeW

        yield


def test_file_real_size(ctypes):
    from filesize.windows import file_real_size

    for file in files:
        assert file_real_size(file) == files[file]

    with pytest.raises(Exception):
        file_real_size("/not_exists/file")


def test_file_real_size_fast(ctypes):
    from filesize.windows import file_real_size_fast

    with tempfile.NamedTemporaryFile("w+b") as file:
        file.write(b"123")
        file.flush()

        files[file.name] = 3

        assert file_real_size_fast(file.name, os.lstat(file.name)) == 3

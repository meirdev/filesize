import os
import tempfile

from filesize.any import file_real_size, file_real_size_fast


def test_file_real_size():
    with tempfile.NamedTemporaryFile("w+b") as file:
        file.write(b"123")
        file.flush()

        assert file_real_size(file.name) == 3


def test_file_real_size_fast():
    with tempfile.NamedTemporaryFile("w+b") as file:
        file.write(b"123")
        file.flush()

        assert file_real_size_fast(file.name, os.lstat(file.name)) == 3

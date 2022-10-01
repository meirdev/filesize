# Ref: https://man7.org/linux/man-pages/man2/stat.2.html

import os

BLOCK_SIZE = 512


def file_real_size(path: str | os.PathLike) -> int:
    return file_real_size_fast(path, os.lstat(path))


def file_real_size_fast(path: str | os.PathLike, stat: os.stat_result) -> int:
    del path
    return stat.st_blocks * BLOCK_SIZE

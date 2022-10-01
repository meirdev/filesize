# Ref: https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getcompressedfilesizew

import ctypes
import os
from ctypes.wintypes import DWORD

NO_ERROR = 0
INVALID_FILE_SIZE = -1  # = DWORD(0xFFFFFFFF)

GetCompressedFileSizeW = ctypes.windll.kernel32.GetCompressedFileSizeW  # type: ignore
GetLastError = ctypes.windll.kernel32.GetLastError  # type: ignore


def file_real_size(path: str | os.PathLike) -> int:
    path = str(path)

    high = DWORD(0)

    if (low := GetCompressedFileSizeW(path, ctypes.byref(high))) == INVALID_FILE_SIZE:
        if (err := GetLastError()) != NO_ERROR:
            raise OSError(f"Last error: {err}")

    return high.value << 32 | low


def file_real_size_fast(path: str | os.PathLike, stat: os.stat_result) -> int:
    del stat
    return file_real_size(path)

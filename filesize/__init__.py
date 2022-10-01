import os

if os.name == "posix":
    from .unix import file_real_size, file_real_size_fast
elif os.name == "nt":
    from .windows import file_real_size, file_real_size_fast
else:
    from .any import file_real_size, file_real_size_fast

size_on_disk = file_real_size
size_on_disk_fast = file_real_size_fast

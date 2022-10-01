# filesize

Cross-platform physical disk space. Inspired by https://github.com/Freaky/rust-filesize.

# Example

```python
import os

from filesize import file_real_size, file_real_size_fast

path = "/path/to/file"

file_real_size(path)
file_real_size_fast(path, os.lstat(path))
```

Human-readable file size:

```python
from filesize.format import Unit, format_unit, format_base

format_base(87653942)  # 87.65 MB
format_unit(87653942, Unit.KB)  # 87653.94 KB
```

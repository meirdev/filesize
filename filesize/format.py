from enum import Enum
from typing import Callable

from .types import uint


class Unit(str, Enum):
    B = "B"
    KB = "KB"
    KiB = "KiB"
    MB = "MB"
    MiB = "MiB"
    GB = "GB"
    GiB = "GiB"
    TB = "TB"
    TiB = "TiB"
    PB = "PB"
    PiB = "PiB"
    EB = "EB"
    EiB = "EiB"
    ZB = "ZB"
    ZiB = "ZiB"


class Base(int, Enum):
    DECIMAL = 1000
    BINARY = 1024


MAPPING_BASE_UNIT: dict[Base, dict[Unit, int]] = {
    Base.DECIMAL: {
        Unit.KB: 1000,
        Unit.MB: 1000**2,
        Unit.GB: 1000**3,
        Unit.TB: 1000**4,
        Unit.PB: 1000**5,
        Unit.EB: 1000**6,
        Unit.ZB: 1000**7,
    },
    Base.BINARY: {
        Unit.KiB: 1024,
        Unit.MiB: 1024**2,
        Unit.GiB: 1024**3,
        Unit.TiB: 1024**4,
        Unit.PiB: 1024**5,
        Unit.EiB: 1024**6,
        Unit.ZiB: 1024**7,
    },
}


FormatCallback = Callable[[float, Unit], str]


def _default_format_function(size: float, unit: Unit) -> str:
    return "{size:.2f} {unit}".format(size=size, unit=unit)


def format_unit(
    file_size: int | uint,
    unit: Unit = Unit.B,
    format_callback: FormatCallback = _default_format_function,
) -> str:
    file_size = float(uint(file_size))

    if unit is not Unit.B:

        if unit in MAPPING_BASE_UNIT[Base.DECIMAL]:
            units = MAPPING_BASE_UNIT[Base.DECIMAL]
        else:
            units = MAPPING_BASE_UNIT[Base.BINARY]

        file_size /= units[unit]

    return format_callback(file_size, unit)


def format_base(
    file_size: int | uint,
    base: Base = Base.DECIMAL,
    format_callback: FormatCallback = _default_format_function,
) -> str:
    file_size = float(uint(file_size))

    units = MAPPING_BASE_UNIT[base]

    prev_unit = Unit.B

    for unit in units:
        if file_size < units[unit]:
            file_size /= units[prev_unit]
            break

        prev_unit = unit

    return format_callback(file_size, prev_unit)

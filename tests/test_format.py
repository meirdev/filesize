from filesize.format import Base, Unit, format_base, format_unit


def test_format_base():
    assert format_base(41_026_764, Base.BINARY) == "39.13 MiB"
    assert format_base(41_026_764, Base.DECIMAL) == "41.03 MB"


def test_format_unit():
    assert format_unit(41_026_764, Unit.B) == "41026764.00 B"
    assert format_unit(41_026_764, Unit.KB) == "41026.76 KB"
    assert format_unit(41_026_764, Unit.MiB) == "39.13 MiB"
    assert format_unit(41_026_764, Unit.GB) == "0.04 GB"


def test_format_callback():
    def _format(size, unit):
        return f"{size:,.2f}{unit[0]}"

    assert format_base(10_378_805_248, format_callback=_format) == "10.38G"
    assert format_unit(10_378_805_248, format_callback=_format) == "10,378,805,248.00B"

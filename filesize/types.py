class UnsignedInt(int):
    def __new__(cls, value: int) -> "UnsignedInt":
        if value < 0:
            raise ValueError("The value must be greater than 0")
        return int.__new__(cls, value)


uint = UnsignedInt

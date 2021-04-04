class Card:
    _suite: str
    _value: str

    @property
    def suite(self) -> str:
        return self._suite

    @property
    def value(self) -> str:
        return self._value

    def __init__(self, *, suite: str, value: str) -> None:
        self._suite = suite
        self._value = value

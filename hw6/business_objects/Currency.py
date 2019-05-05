
class Currency:
    _label = ''
    _description = ''
    _rate: int = 0

    def __init__(self, label: str, description: str):
        self._label = label
        self._description = description

    def set_rate(self, rate: int):
        self._rate = rate

    @property
    def label(self):
        return self._label

    @property
    def description(self):
        return self._description

    @property
    def rate(self):
        return self._rate

    def __repr__(self) -> str:
        return f'{self._label} - {self._description} - {self._rate}'

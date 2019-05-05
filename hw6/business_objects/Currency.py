class Currency:
    _label = ''
    _description = ''

    def __init__(self, label, description):
        self._label = label
        self._description = description

    @property
    def label(self):
        return self._label

    @property
    def description(self):
        return self._description

    def __repr__(self) -> str:
        return f'{self._label} - {self._description}'



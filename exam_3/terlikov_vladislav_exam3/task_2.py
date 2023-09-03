class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, value):
        self._kg = value

    def to_pounds(self):
        return self._kg * 2.20462


k = KgToPounds(10)
print(k.kg)
k.kg = 20
print(k.kg)
print(k.to_pounds())

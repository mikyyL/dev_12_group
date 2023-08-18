class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        self._kg = new_kg

    def to_pounds(self):
        return self._kg * 2.20462


kg_to_pounds = KgToPounds(10)
print(kg_to_pounds.kg)

kg_to_pounds.kg = 20
print(kg_to_pounds.to_pounds())
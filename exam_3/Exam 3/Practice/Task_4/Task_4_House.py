class House:

    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        # discount = float(input('Enter the discount in %: '))
        fin_price = self._price * ((100 - discount)/100)
        return fin_price

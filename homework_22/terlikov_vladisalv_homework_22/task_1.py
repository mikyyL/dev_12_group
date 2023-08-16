import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return f'letter {letter} in EngAlphabet'
        return f'letter {letter} not EngAlphabet'

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("Eng txt example:\n'Favorite or profitable profession'")


eng = EngAlphabet()
eng.print()
letter_en = input('Enter letter: ')
print(eng.is_en_letter(letter_en))
print(eng.letters_num())
eng.example()

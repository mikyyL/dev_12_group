# 1. Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе он будет
# возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'A Way with Words is a radio show and podcast that features' \
               'light-hearted conversation about language change, debates,' \
               'and differences, as well as new words, old sayings, slang,' \
               'family expressions, word origins and histories'


eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('a'))
print(eng_alphabet.is_en_letter('ы'))
print(EngAlphabet.example())



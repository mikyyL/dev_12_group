class TestLessonPytest:

    def test_one(self):
        num1 = 1
        assert num1 != 0, 'ожидалось число не 0'

    def test_two(self):
        num = 3
        assert num != 2, 'ожидалось число не два'

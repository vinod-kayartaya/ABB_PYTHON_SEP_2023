import unittest
from vinutils import factorial


class TestFactorial(unittest.TestCase):
    def test_should_get_factorial_of_positive_number(self):
        arg = 5
        expected = 120
        actual = factorial(arg)
        self.assertEqual(expected, actual)

    def test_should_get_factorial_of_0(self):
        self.assertEqual(1, factorial(0))

    def test_should_raise_error_for_non_int(self):
        # try:
        #     factorial(1.23)
        #     self.fail('expected to cause an error. but no error was raised.')
        # except TypeError:
        #     pass
        def fn():
            factorial(1.23)
        self.assertRaises(TypeError, fn)


if __name__ == '__main__':
    unittest.main()

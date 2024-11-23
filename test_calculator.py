import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    
        self.assertEqual(self.calc.add(34, 1), 35)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(8, 4), 32)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(40, 8), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(17, 3), 2)
    
    
if __name__ == '__main__':
    unittest.main()
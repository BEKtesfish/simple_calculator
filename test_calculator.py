import unittest
from calculator import Calculator
class TestCalc(unittest.TestCase):
    def test_add(self):
        result=Calculator.add(2,2)
        self.assertEqual(result,4)
    
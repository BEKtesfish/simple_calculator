import unittest
from calculator import Calculator
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc=Calculator()



    def test_add(self):
        result=self.calc.add(2,2)
        self.assertEqual(result,'2 + 2 = 4')
        result=self.calc.add(5,5)
        self.assertEqual(result,'5 + 5 = 10')
        
        
        
    def test_subtract(self):
        result=self.calc.subtract(2,2)
        self.assertEqual(result,'2 - 2 = 0')
        result=self.calc.subtract(100,50)
        self.assertEqual(result,'100 - 50 = 50')


    def test_multi(self):
        result=self.calc.multiply(2,2)
        self.assertEqual(result,'2 * 2 = 4')
        result=self.calc.multiply(8,8)
        self.assertEqual(result,'8 * 8 = 64')


    def test_division(self):
        result=self.calc.divide(2,2)
        self.assertEqual(result,'2 / 2 = 1.0')
        result=self.calc.divide(0,2)
        self.assertEqual(result,'0 / 2 = 0.0')
        with self.assertRaises(AssertionError):
            self.calc.divide(2,0)

    def test_instance(self):
        self.assertIsInstance(self.calc,Calculator)

if __name__== '__main__':
    unittest.main()
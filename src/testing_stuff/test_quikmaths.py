import unittest
from quikmaths import *

class QuikMathTests(unittest.TestCase):

    def test_addition(self):
        self.assertEquals(addition(2, 4), 6)
    
    def test_multiplication(self):
        self.assertEquals(multiplication(2, 8), 16)

    def test_subtraction(self):
        self.assertEquals(subtraction(5, 3), 2)
import unittest
from Arith import Arith

class ArithTests(unittest.TestCase):
    def test_add(self):
        a = Arith()
        self.assertEqual(a.add(3,2), 5)
    def test_sub(self):
        a = Arith()
        self.assertEqual(a.sub(5,2), 3)

if __name__ == '__main__':
    unittest.main()

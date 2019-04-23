import unittest
from MySort import mysort

class MySortTests(unittest.TestCase):
    def test_mysort(self):
        self.assertEqual(mysort([2,37,500,16]), [2, 16, 37, 500])

if __name__ == '__main__':
    unittest.main()
import unittest
from MySearch import mysearch

class MySearchTests(unittest.TestCase):
    def test_mysearch(self):
        self.assertEqual(mysearch([2,37,500,16], 18), -1)
        self.assertEqual(mysearch([2, 37, 500, 16], 500), 2)

if __name__ == '__main__':
    unittest.main()

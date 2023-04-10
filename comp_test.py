import unittest
from brute_force import bf

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(bf(), False)


if __name__ == '__main__':
    unittest.main()

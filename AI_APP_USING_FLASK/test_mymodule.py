import unittest

from mymodule import square, doubler
class TestMyModule(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(15), 225)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-3), 9)

    def test_doubler(self):
        self.assertEqual(doubler(3), 6)

if __name__ == '__main__':
    unittest.main()

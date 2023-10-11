import unittest
import sys
sys.path.append('..')
from CodeChallenges import array_reverse

class TestArrayReverse(unittest.TestCase):

    def test_reverse_array(self):
        self.assertEqual(array_reverse.reverse_array([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
        self.assertEqual(array_reverse.reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12]), [-12, 823, -923, 10, 23, 3546, 2354, 89])
        self.assertEqual(array_reverse.reverse_array([]), [])
        self.assertEqual(array_reverse.reverse_array([1]), [1])
        self.assertEqual(array_reverse.reverse_array(['a', 'b', 'c']), ['c', 'b', 'a'])

if __name__ == '__main__':
    unittest.main()
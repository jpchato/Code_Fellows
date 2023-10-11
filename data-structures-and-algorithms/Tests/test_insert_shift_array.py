import unittest
import sys
sys.path.append('..')
from CodeChallenges import insert_shift_array  

class TestInsertShiftArray(unittest.TestCase):
    
    def test_insert_shift_array_even_length(self):
        self.assertEqual(insert_shift_array.shift_array_insert([2, 4, 6, -8], 5), [2, 4, 5, 6, -8])
    
    def test_insert_shift_array_odd_length(self):
        self.assertEqual(insert_shift_array.shift_array_insert([42, 8, 15, 23, 42], 16), [42, 8, 15, 16, 23, 42])
    
    def test_insert_shift_array_empty(self):
        self.assertEqual(insert_shift_array.shift_array_insert([], 5), [5])
    
    def test_insert_shift_array_single_element(self):
        self.assertEqual(insert_shift_array.shift_array_insert([1], 5), [1, 5])

if __name__ == "__main__":
    unittest.main()

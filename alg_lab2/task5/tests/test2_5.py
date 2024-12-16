import unittest
import time
import tracemalloc
from alg_lab2.task5.src.task5 import is_majority_element
import utils

class TestMajorityElement(unittest.TestCase):

    def test_is_majority_element(self):
        # Given
        arr = [1, 2, 3, 3, 3, 4, 3, 5, 3]
        # When
        result = is_majority_element(arr)
        # Then
        self.assertTrue(result) 

    def test_performance(self):
        # Given
        arr = [3] * 100000 + [1] * 500000
        # When
        start_time = time.time()
        result = is_majority_element(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)
    def test_memory(self):
        # Given
        arr = [3] * 100000 + [1] * 500000
        tracemalloc.start()
        # When
        result = is_majority_element(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)  

if __name__ == "__main__":
    unittest.main()

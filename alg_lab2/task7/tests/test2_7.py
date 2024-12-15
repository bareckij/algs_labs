import unittest
import time
import tracemalloc
from alg_lab2.task7.src.task7 import find_max_subarray
import utils

class TestMaxSubarray(unittest.TestCase):

    def test_performance(self):
        # Given
        arr = [1] * 10000
        # When
        start_time = time.time()
        result = find_max_subarray(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)  

        # Given
        tracemalloc.start()
        # When
        result = find_max_subarray(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)  

if __name__ == "__main__":
    unittest.main()

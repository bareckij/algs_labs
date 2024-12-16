import unittest
import time
import tracemalloc
from alg_lab2.task1.src.task1 import merge_sort
import utils

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        # Given
        n = 5
        arr = [3, 1, 4, 1, 5]
        expected = [1, 1, 3, 4, 5]
        # When
        result = merge_sort(arr, 0, n - 1)
        # Then
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        arr = [i for i in range(10000, 0, -1)]
        n = len(arr)
        # When
        start_time = time.time()
        merge_sort(arr, 0, n - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

    def test_memory(self):
        # Given
        arr = [i for i in range(10000, 0, -1)]
        n = len(arr)
        tracemalloc.start()
        # When
        merge_sort(arr, 0, n - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

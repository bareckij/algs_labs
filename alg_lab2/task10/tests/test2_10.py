import unittest
import time
import tracemalloc
from alg_lab2.task10.src.task10 import merge_sort
import utils

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        # Given
        n, arr = utils.read_data_from_file('alg_lab2/task10/textf/input.txt')
        # When
        result = merge_sort(arr, 0, n-1)
        # Then
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        n, arr = utils.read_data_from_file('alg_lab2/task10/textf/input.txt')
        # When
        start_time = time.time()
        merge_sort(arr, 0, n-1)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)
    def test_memory(self):
        # Given
        tracemalloc.start()
        # When
        merge_sort(arr, 0, n-1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

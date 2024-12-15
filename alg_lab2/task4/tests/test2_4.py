import unittest
import time
import tracemalloc
from alg_lab2.task4.src.task4 import binary_search
import utils

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        # Given
        n = 5
        arr = [1, 3, 5, 7, 9]
        search_nums = [3, 6, 9]
        expected = [1, -1, 4]  
        # When
        results = [binary_search(arr, num) for num in search_nums]
        # Then
        self.assertEqual(results, expected)

        # Given
        n = 6
        arr = [2, 4, 6, 8, 10, 12]
        search_nums = [4, 11, 12]
        expected = [1, -1, 5]  
        # When
        results = [binary_search(arr, num) for num in search_nums]
        # Then
        self.assertEqual(results, expected)

        # Given
        n = 4
        arr = [1, 2, 3, 4]
        search_nums = [0, 5]
        expected = [-1, -1] 
        # When
        results = [binary_search(arr, num) for num in search_nums]
        # Then
        self.assertEqual(results, expected)

    def test_performance(self):
        # Given
        arr = [i for i in range(1000000)]
        search_nums = [500, 1000000, 999999]
        # When
        start_time = time.time()
        results = [binary_search(arr, num) for num in search_nums]
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # Given
        tracemalloc.start()
        # When
        results = [binary_search(arr, num) for num in search_nums]
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

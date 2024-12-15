import unittest
import time
import tracemalloc
from io import StringIO
from contextlib import redirect_stdout
from alg_lab1.task1.src.task1 import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        # Given
        nums = [5, 3, 8, 1, 2]
        expected = [1, 2, 3, 5, 8]
        # When
        result = insertion_sort(nums)
        # Then
        self.assertEqual(result, expected)

    def test_empty_list(self):
        # Given
        nums = []
        expected = []
        # When
        result = insertion_sort(nums)
        # Then
        self.assertEqual(result, expected)

    def test_single_element_list(self):
        # Given
        nums = [42]
        expected = [42]
        # When
        result = insertion_sort(nums)
        # Then
        self.assertEqual(result, expected)

    def test_large_input(self):
        # Given
        nums = list(range(1000, 0, -1))  
        expected = list(range(1, 1001))  
        # When
        start_time = time.time()
        result = insertion_sort(nums)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertEqual(result, expected)
        self.assertLess(execution_time, 1)  

    def test_performance_memory_usage(self):
        # Given
        nums = [i for i in range(1, 101)]
        tracemalloc.start()
        # When
        start_time = time.time()
        insertion_sort(nums)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)  
        self.assertLess(peak / 10**6, 50)  




if __name__ == "__main__":
    unittest.main()

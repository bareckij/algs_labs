import unittest
import time
import tracemalloc
from alg_lab4.task7.src.task7 import sliding_window_maximum
import utils


class TestTask7(unittest.TestCase):

    def test_sliding_window_maximum(self):
        # Given
        arr = [7, 7, 5, 6, 6, 2, 7, 3]
        n = 8
        m = 4
        expected_output = [7, 7, 6, 7, 7]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_same_elements(self):
        # Given
        arr = [4, 4, 4, 4, 4]
        n = 5
        m = 3
        expected_output = [4, 4, 4]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_one_element(self):
        # Given
        arr = [5]
        n = 1
        m = 1
        expected_output = [5]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_decreasing(self):
        # Given
        arr = [9, 8, 7, 6, 5, 4]
        n = 6
        m = 3
        expected_output = [9, 8, 7, 6]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_increasing(self):
        # Given
        arr = [1, 2, 3, 4, 5, 6]
        n = 6
        m = 2
        expected_output = [2, 3, 4, 5, 6]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_minimum(self):
        # Given
        arr = [0, 0, 0, 0, 0]
        n = 5
        m = 3
        expected_output = [0, 0, 0]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_maximum(self):
        # Given
        arr = [100000, 99999, 99998, 100000]
        n = 4
        m = 2
        expected_output = [100000, 99999, 100000]
        # When
        result = sliding_window_maximum(arr, n, m)
        # Then
        self.assertEqual(result, expected_output)

    def test_performance(self):
        # Given
        arr = [i for i in range(1, 10001)]
        n = 10000
        m = 1000
        # When
        start_time = time.time()
        sliding_window_maximum(arr, n, m)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # When measuring memory
        tracemalloc.start()
        sliding_window_maximum(arr, n, m)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)  # Memory usage should be less than 256 MB


if __name__ == "__main__":
    unittest.main()

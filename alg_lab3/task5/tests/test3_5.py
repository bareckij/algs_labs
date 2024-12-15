import unittest
import time
import tracemalloc
from alg_lab3.task5.src.task5 import h_index
import utils

class TestHIndex(unittest.TestCase):

    def test_h_index(self):
        # Given
        arr = [3, 0, 6, 1, 5, 2]
        expected = 3
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = []
        expected = 0
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = [1]
        expected = 1
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = [5, 5, 5, 5, 5]
        expected = 5
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = [100] * 1000
        expected = 100
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = [1, 2, 3, 4, 5]
        expected = 3
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr = [0, 0, 0, 0]
        expected = 0
        # When
        result = h_index(arr)
        # Then
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        arr = [i for i in range(100)]
        # When
        start_time = time.time()
        h_index(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # Given
        tracemalloc.start()
        # When
        h_index(arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

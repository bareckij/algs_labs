import unittest
import time
import tracemalloc
from alg_lab3.task4.src.task4 import count_intervals
import utils

class TestCountIntervals(unittest.TestCase):

    def test_count_intervals(self):
        # Given
        data = [(1, 5), (2, 6), (3, 7)]
        expected = [1, 0]
        # When
        result = count_intervals(data)
        # Then
        self.assertEqual(result, expected)

        # Given
        data = [(1, 3), (5, 7), (8, 10)]
        expected = [0, 0]
        # When
        result = count_intervals(data)
        # Then
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        data = [(i, i + 1) for i in range(100)]
        # When
        start_time = time.time()
        count_intervals(data)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # Given
        tracemalloc.start()
        # When
        count_intervals(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

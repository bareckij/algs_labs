import unittest
import time
import tracemalloc
from io import StringIO
from contextlib import redirect_stdout
from alg_lab1.task4.src.task4 import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        # Given
        numbers = [1, 2, 3, 4, 5, 3, 6, 3]
        target = 3
        expected_indexes = [2, 5, 7]
        expected_count = 3

        # When
        indexes, count = linear_search(numbers, target)

        # Then
        self.assertEqual(indexes, expected_indexes)
        self.assertEqual(count, expected_count)

    def test_empty_list(self):
        # Given
        numbers = []
        target = 3
        expected_indexes = []
        expected_count = 0

        # When
        indexes, count = linear_search(numbers, target)

        # Then
        self.assertEqual(indexes, expected_indexes)
        self.assertEqual(count, expected_count)

    def test_target_not_found(self):
        # Given
        numbers = [1, 2, 3, 4, 5]
        target = 6
        expected_indexes = []
        expected_count = 0

        # When
        indexes, count = linear_search(numbers, target)

        # Then
        self.assertEqual(indexes, expected_indexes)
        self.assertEqual(count, expected_count)

    def test_single_occurrence(self):
        # Given
        numbers = [1, 2, 3, 4, 5]
        target = 3
        expected_indexes = [2]
        expected_count = 1

        # When
        indexes, count = linear_search(numbers, target)

        # Then
        self.assertEqual(indexes, expected_indexes)
        self.assertEqual(count, expected_count)

    def test_performance(self):
        # Given
        numbers = [i for i in range(1, 10001)]
        target = 5000

        # When
        start_time = time.time()
        linear_search(numbers, target)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        self.assertLess(execution_time, 1)

    def test_memory_usage(self):
        # Given
        numbers = [i for i in range(1, 101)]
        target = 5000

        # When
        tracemalloc.start()
        start_time = time.time()
        linear_search(numbers, target)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = end_time - start_time

        # Then
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10**6, 50)



if __name__ == "__main__":
    unittest.main()

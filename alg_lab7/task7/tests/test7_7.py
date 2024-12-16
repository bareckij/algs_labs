import unittest
import time
import tracemalloc
from alg_lab7.task7.src.task7_7 import is_match

class TestIsMatch(unittest.TestCase):

    def test_is_match(self):
        # Given
        pattern = "k?t*n"
        string = "kitten"
        # When
        result = is_match(pattern, string)
        # Then
        self.assertTrue(result)

    def test_performance_is_match(self):
        # Given
        pattern = "a" * 100
        string = "a" * 100
        # When
        start_time = time.time()
        result = is_match(pattern, string)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        tracemalloc.start()
        result = is_match(pattern, string)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

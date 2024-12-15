import unittest
import time
import tracemalloc
from alg_lab7.task5.src.task7_5 import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_longest_common_subsequence(self):
        # Given
        a = "AGGT12AB"
        b = "12TXAYB"
        c = "12XBA"
        # When
        result = longest_common_subsequence(a, b, c)
        # Then
        self.assertEqual(result, 3)

        # Given
        a = "AXYT"
        b = "AYZX"
        c = "AXZ"
        # When
        result = longest_common_subsequence(a, b, c)
        # Then
        self.assertEqual(result, 2)

        # Given
        a = "AAAA"
        b = "AA"
        c = "A"
        # When
        result = longest_common_subsequence(a, b, c)
        # Then
        self.assertEqual(result, 1)

        # Given
        a = "abcde"
        b = "fbdam"
        c = "abdf"
        # When
        result = longest_common_subsequence(a, b, c)
        # Then
        self.assertEqual(result, 2)

        # Given
        a = "abcdef"
        b = "abcdef"
        c = "abcdef"
        # When
        result = longest_common_subsequence(a, b, c)
        # Then
        self.assertEqual(result, 6)

    def test_performance_longest_common_subsequence(self):
        # Given
        a = "A" * 100
        b = "B" * 100
        c = "C" * 100
        # When
        start_time = time.time()
        result = longest_common_subsequence(a, b, c)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        tracemalloc.start()
        result = longest_common_subsequence(a, b, c)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

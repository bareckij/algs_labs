import unittest
import time
import tracemalloc
from alg_lab7.task4.src.task7_4 import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_longest_common_subsequence(self):
        # Given
        a = "ABCBDAB"
        b = "BDCAB"
        # When
        result = longest_common_subsequence(a, b)
        # Then
        self.assertEqual(result, 4)

        # Given
        a = "AGGTAB"
        b = "GXTXAYB"
        # When
        result = longest_common_subsequence(a, b)
        # Then
        self.assertEqual(result, 4)

        # Given
        a = "AXYT"
        b = "AYZX"
        # When
        result = longest_common_subsequence(a, b)
        # Then
        self.assertEqual(result, 2)

        # Given
        a = "AAAA"
        b = "AA"
        # When
        result = longest_common_subsequence(a, b)
        # Then
        self.assertEqual(result, 2)

        # Given
        a = "abcdef"
        b = "fbdam"
        # When
        result = longest_common_subsequence(a, b)
        # Then
        self.assertEqual(result, 2)

    def test_performance_longest_common_subsequence(self):
        # Given
        a = "A" * 1000
        b = "B" * 1000
        # When
        start_time = time.time()
        result = longest_common_subsequence(a, b)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        tracemalloc.start()
        result = longest_common_subsequence(a, b)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

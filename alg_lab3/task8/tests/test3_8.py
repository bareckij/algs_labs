import unittest
import time
import tracemalloc
from alg_lab3.task8.src.task8 import find_k_nearest_points
import utils

class TestFindKNearestPoints(unittest.TestCase):

    def test_find_k_nearest_points(self):
        # Given
        points = [(3, 3), (5, -1), (-2, 4)]
        k = 2
        expected = [(3, 3), (-2, 4)]
        # When
        result = find_k_nearest_points(points, k)
        # Then
        self.assertEqual(result, expected)

        # Given
        points = [(10, 10)]
        k = 1
        expected = [(10, 10)]
        # When
        result = find_k_nearest_points(points, k)
        # Then
        self.assertEqual(result, expected)

        # Given
        points = [(0, 0), (0, 0), (0, 0)]
        k = 2
        expected = [(0, 0), (0, 0)]
        # When
        result = find_k_nearest_points(points, k)
        # Then
        self.assertEqual(result, expected)

        # Given
        points = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        k = 2
        expected = [(1, 1), (-1, -1)]
        # When
        result = find_k_nearest_points(points, k)
        # Then
        self.assertTrue(set(result) == set(expected))

    def test_performance(self):
        # Given
        points = [(i, i) for i in range(100)]
        k = 1000
        # When
        start_time = time.time()
        find_k_nearest_points(points, k)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # Given
        tracemalloc.start()
        # When
        find_k_nearest_points(points, k)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

import unittest
import time
import tracemalloc
from alg_lab5.task2.src.task2 import calculate_tree_height

class TestTask2(unittest.TestCase):

    def test_should_calculate_tree_height(self):
        # Given
        n = 5
        parents = [-1, 4, 4, 1, 1]
        # When
        height = calculate_tree_height(n, parents)
        # Then
        self.assertEqual(height, 1)

    def test_performance_calculate_tree_height(self):
        # Given
        n = 10000
        parents = [-1] + [i % 100 for i in range(1, n)]
        # When
        start_time = time.time()
        calculate_tree_height(n, parents)
        end_time = time.time()
        execution_time = end_time - start_time

        # When
        tracemalloc.start()
        calculate_tree_height(n, parents)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 3)
        self.assertLess(peak / 10**6, 512)

if __name__ == '__main__':
    unittest.main()

import unittest
import time
import tracemalloc
from alg_lab5.task4.src.task4 import build_min_heap

class TestTask4(unittest.TestCase):
    
    def test_build_min_heap(self):
        # Given
        arr = [5, 4, 3, 2, 1]
        # When
        swaps = build_min_heap(arr)
        # Then
        expected_arr = [1, 2, 3, 5, 4]
        expected_swaps = [(1, 4), (0, 1), (1, 3)]
        self.assertEqual(arr, expected_arr)
        self.assertEqual(swaps, expected_swaps)

    def test_performance_min_heapify(self):
        # Given
        array = [i for i in range(1000, 0, -1)]
        # When
        start_time = time.time()
        build_min_heap(array)
        end_time = time.time()
        execution_time = end_time - start_time
        # When
        tracemalloc.start()
        build_min_heap(array)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        self.assertLess(execution_time, 3)
        self.assertLess(peak / 10**6, 512)

if __name__ == '__main__':
    unittest.main()

import unittest
import time
import tracemalloc
from alg_lab5.task1.src.task1 import is_non_decreasing_heap  

class TestTask1(unittest.TestCase):

    def test_should_be_non_decreasing_heap(self):
        # Тест 1: Проверка корректности для небольшой пирамиды
        n = 5
        arr = [0, 1, 2, 5, 10]
        expected_result = "YES"
        result = is_non_decreasing_heap(n, arr)
        self.assertEqual(result, expected_result)

        # Тест 2: Проверка для массива, который не является пирамидой
        n = 5
        arr = [3, 2, 1, 0, 1]
        expected_result = "NO"
        result = is_non_decreasing_heap(n, arr)
        self.assertEqual(result, expected_result)

    def test_performance_non_decreasing_heap(self):
        # Given
        n = 1000000
        arr = [i for i in range(n - 1, -1, -1)] 
        # When
        start_time = time.time()
        result = is_non_decreasing_heap(n, arr)
        end_time = time.time()
        execution_time = end_time - start_time

        # When
        tracemalloc.start()
        result = is_non_decreasing_heap(n, arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 2)  
        self.assertLess(peak / 10**6, 256)  

if __name__ == '__main__':
    unittest.main()
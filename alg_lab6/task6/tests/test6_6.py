import unittest
import time
import tracemalloc
from alg_lab6.task6.src.task6_6 import process_fibonacci_check, is_fibonacci

class TestTask6(unittest.TestCase):

    def test_should_process_fibonacci_check(self):
        # Given
        queries = ['8', '1', '2', '3', '4', '5', '6', '7', '13']
        # When
        result = process_fibonacci_check(queries)
        # Then
        expected_result = ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
        self.assertEqual(result, expected_result)

        # Given
        queries = ['0', '144', '233', '100', '6765']
        # When
        result = process_fibonacci_check(queries)
        # Then
        expected_result = ['Yes', 'Yes', 'Yes', 'No', 'Yes']
        self.assertEqual(result, expected_result)

    def test_performance_fibonacci_check(self):
        # Given
        queries = [str(i) for i in range(1, 1000000)]
        
        # When
        start_time = time.time()
        result = process_fibonacci_check(queries)
        end_time = time.time()
        execution_time = end_time - start_time

        # When
        tracemalloc.start()
        result = process_fibonacci_check(queries)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

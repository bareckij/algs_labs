import unittest
import time
import tracemalloc
from alg_lab6.task1.src.task6_1 import process_operations

class TestTask1(unittest.TestCase):

    def test_should_process_operations(self):
        # Given
        n = 5
        operations = [
            "A 1",
            "A 2",
            "? 1",
            "? 3",
            "D 1",
            "? 1",
        ]
        # When
        result = process_operations(n, operations)
        # Then
        expected_result = ['Y', 'N', 'N']
        self.assertEqual(result, expected_result)


    def test_performance_process_operations(self):
        # Given
        n = 1000000
        operations = []
        for i in range(n):
            operations.append(f"A {i}")
        for i in range(n):
            operations.append(f"? {i}")
        
        # When
        start_time = time.time()
        result = process_operations(n, operations)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # When
        tracemalloc.start()
        result = process_operations(n, operations)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Then
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

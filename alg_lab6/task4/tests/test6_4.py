import unittest
import time
import tracemalloc
from alg_lab6.task4.src.task6_4 import process_operations, AssociativeArray

class TestTask4(unittest.TestCase):

    def test_should_process_operations(self):
        # Given
        operations = [
            "put a 1", 
            "put b 2", 
            "put c 3", 
            "get a", 
            "prev b", 
            "next b", 
            "delete b", 
            "get b", 
            "prev c", 
            "next a"
        ]
        # When
        result = process_operations(len(operations), operations)
        # Then
        expected_result = ['1', '1', '3', '<none>', '1', '3']
        self.assertEqual(result, expected_result)

        # Given
        operations = [
            "put x 100",
            "put y 200",
            "get x",
            "delete x",
            "get x",
            "get y"
        ]
        # When
        result = process_operations(len(operations), operations)
        # Then
        expected_result = ['100', '<none>', '200']
        self.assertEqual(result, expected_result)

    def test_performance_process_operations(self):
        # Given
        n = 1000000
        operations = []
        for i in range(n):
            operations.append(f"put key{i} value{i}")
        for i in range(n):
            operations.append(f"get key{i}")
        
        # When
        start_time = time.time()
        result = process_operations(n * 2, operations)
        end_time = time.time()
        execution_time = end_time - start_time

        # When
        tracemalloc.start()
        result = process_operations(n * 2, operations)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

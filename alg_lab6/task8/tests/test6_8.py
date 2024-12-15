import unittest
import time
import tracemalloc
from alg_lab6.task8.src.task6_8 import process_operations

class TestTask8(unittest.TestCase):

    def test_should_process_operations(self):
        # Given
        N = 3
        X = 20
        A = 6
        B = 8
        AC = 2
        BC = 3
        AD = 4
        BD = 5
        
        # When
        result = process_operations(N, X, A, B, AC, BC, AD, BD)
        
        # Then
        expected_result = (54023, 18, 23)  
        self.assertEqual(result, expected_result)

    def test_performance_operations(self):
        # Given
        N = 1000000
        X = 100
        A = 10
        B = 5
        AC = 1
        BC = 2
        AD = 3
        BD = 4
        
        # When
        start_time = time.time()
        result = process_operations(N, X, A, B, AC, BC, AD, BD)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # When
        tracemalloc.start()
        result = process_operations(N, X, A, B, AC, BC, AD, BD)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        
        self.assertLess(execution_time, 2)  
        self.assertLess(peak / 10**6, 256)  

if __name__ == '__main__':
    unittest.main()

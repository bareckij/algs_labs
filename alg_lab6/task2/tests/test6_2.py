import unittest
import time
import tracemalloc
from alg_lab6.task2.src.task6_2 import process_phonebook_queries

class TestTask2(unittest.TestCase):

    def test_should_process_phonebook_queries(self):
        # Given
        n = 5
        queries = [
            "add 123456 John",
            "add 789012 Alice",
            "find 123456",
            "find 111111",
            "del 123456",
            "find 123456",
        ]
        # When
        result = process_phonebook_queries(n, queries)
        # Then
        expected_result = ['John', 'not found', 'not found']
        self.assertEqual(result, expected_result)

    def test_performance_process_phonebook_queries(self):
        # Given
        n = 1000000
        queries = []
        for i in range(n):
            queries.append(f"add {i} Name_{i}")
        for i in range(n):
            queries.append(f"find {i}")
        # When
        start_time = time.time()
        result = process_phonebook_queries(n, queries)
        end_time = time.time()
        execution_time = end_time - start_time
        # When
        tracemalloc.start()
        result = process_phonebook_queries(n, queries)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

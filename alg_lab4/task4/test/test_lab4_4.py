import unittest
import time
import tracemalloc
from alg_lab4.task4.src.task4 import check_brackets
from alg_lab4.task4.src.task4 import process_brackets

class TestTask4(unittest.TestCase):

    def test_check_brackets(self):
        # Given
        input_str = "([])foo(bar[i);]"
        # When
        result = check_brackets(input_str)
        # Then
        expected = "14"
        self.assertEqual(result, expected)

    def test_right(self):
        # Given
        input_str = "([]){[()]}"
        # When
        result = check_brackets(input_str)
        # Then
        expected = "Success"
        self.assertEqual(result, expected)

    def test_wrong(self):
        # Given
        input_str = "([)]"
        # When
        result = check_brackets(input_str)
        # Then
        expected = "3"
        self.assertEqual(result, expected)

    def test_another(self):
        # Given
        input_str = "([}}"
        # When
        result = check_brackets(input_str)
        # Then
        expected = "3"
        self.assertEqual(result, expected)

    def test_empty(self):
        # Given
        input_str = ""
        # When
        result = check_brackets(input_str)
        # Then
        expected = "Success"
        self.assertEqual(result, expected)

    def test_performance_check_brackets(self):
        # Given
        input_str = "()" * 10000  # Большая строка для тестирования производительности
        # When
        start_time = time.time()
        check_brackets(input_str)
        end_time = time.time()
        execution_time = end_time - start_time
        # When
        tracemalloc.start()
        check_brackets(input_str)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

import unittest
import time
import tracemalloc
from alg_lab4.task8.src.task8 import evaluate_postfix_expression
import utils

class TestTask8(unittest.TestCase):

    def test_evaluate_postfix_expression(self):
        # Given
        expression = ['8', '9', '+']
        expected = 17  # 8 + 9 = 17
        # When
        result = evaluate_postfix_expression(len(expression), expression)
        # Then
        self.assertEqual(result, expected)

    def test_several_operation(self):
        # Given
        expression = ['8', '9', '+', '1', '7', '-', '*']
        expected = -102  # (8 + 9) * (1 - 7) = 17 * (-6) = -102
        # When
        result = evaluate_postfix_expression(len(expression), expression)
        # Then
        self.assertEqual(result, expected)

    def test_negative_number(self):
        # Given
        expression = ['5', '3', '-', '10', '2', '-', '*']
        expected = 16  # (5 - 3) * (10 - 2) = 2 * 8 = 16
        # When
        result = evaluate_postfix_expression(len(expression), expression)
        # Then
        self.assertEqual(result, expected)

    def test_one_number(self):
        # Given
        expression = ['42']
        expected = 42  # Один операнд - сам результат
        # When
        result = evaluate_postfix_expression(len(expression), expression)
        # Then
        self.assertEqual(result, expected)

    def test_more_harder(self):
        # Given
        expression = ['2', '3', '4', '+', '*', '5', '+']
        expected = 19  # 2 * (3 + 4) + 5 = 2 * 7 + 5 = 14 + 5 = 19
        # When
        result = evaluate_postfix_expression(len(expression), expression)
        # Then
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        expression = ['1000', '2000', '+', '3000', '5000', '+', '4000', '+']
        # When measuring time
        start_time = time.time()
        evaluate_postfix_expression(len(expression), expression)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # When measuring memory
        tracemalloc.start()
        evaluate_postfix_expression(len(expression), expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)  # Memory usage should be less than 256 MB


if __name__ == "__main__":
    unittest.main()

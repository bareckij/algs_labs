import unittest
import time
import tracemalloc
from alg_lab3.task6.src.task import sum_of_every_tenth_product
import utils

class TestSumOfEveryTenthProduct(unittest.TestCase):

    def test_sum_of_every_tenth_product(self):
        # Given
        arr_a = [7, 1, 4, 9]
        arr_b = [2, 7, 8, 11]
        expected = 51
        # When
        result = sum_of_every_tenth_product(arr_a, arr_b)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr_a = []
        arr_b = []
        expected = 0
        # When
        result = sum_of_every_tenth_product(arr_a, arr_b)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr_a = [5]
        arr_b = [5]
        expected = 25
        # When
        result = sum_of_every_tenth_product(arr_a, arr_b)
        # Then
        self.assertEqual(result, expected)

        # Given
        arr_a = [1, 1, 1]
        arr_b = [1, 1, 1]
        expected = 1
        # When
        result = sum_of_every_tenth_product(arr_a, arr_b)
        # Then
        self.assertEqual(result, expected)

    def test_performance(self):
        # Given
        arr_a = [i for i in range(100000)]
        arr_b = [i for i in range(100000)]
        # When
        start_time = time.time()
        sum_of_every_tenth_product(arr_a, arr_b)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # Given
        tracemalloc.start()
        # When
        sum_of_every_tenth_product(arr_a, arr_b)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

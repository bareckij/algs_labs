import unittest
import time
import tracemalloc
from alg_lab7.task1.src.task7_1 import process_operations

class test_shouldCoinChange(unittest.TestCase):

    def test_should_should_coin_change_unlimited(self):
        # Given
        money = 6
        k = 3
        coins = [1, 3, 4]
        # When
        result = process_operations(money, k, coins)
        # Then
        self.assertEqual(result, 2)

    def test_should_coin_change_limited(self):
        # Given
        money = 6
        k = 3
        coins = [1, 3, 4]
        counts = [2, 1, 1]
        # When
        result = process_operations(money, k, coins, counts)
        # Then
        self.assertEqual(result, 3)


    def test_performance_coin_change_unlimited(self):
        # Given
        money = 1000
        k = 100
        coins = [i for i in range(1, k + 1)]
        # When
        start_time = time.time()
        result = process_operations(money, k, coins)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        tracemalloc.start()
        result = process_operations(money, k, coins)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

    def test_performance_coin_change_limited(self):
        # Given
        money = 1000
        k = 100
        coins = [i for i in range(1, k + 1)]
        counts = [10] * k
        # When
        start_time = time.time()
        result = process_operations(money, k, coins, counts)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        tracemalloc.start()
        result = process_operations(money, k, coins, counts)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()

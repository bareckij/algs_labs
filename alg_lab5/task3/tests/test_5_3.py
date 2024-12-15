import unittest
import time
import tracemalloc
from alg_lab5.task3.src.task3 import process_packets
import utils

class TestTask3(unittest.TestCase):

    def test_should_process_packets_correctly(self):
        # Given
        S = 1
        n = 2
        packets = [(0, 1), (0, 1)]
        # When
        result = process_packets(S, n, packets)
        # Then
        self.assertEqual(result, [0, -1])

    def test_should_process_packets_correctly_multiple(self):
        # Given
        S = 2
        n = 3
        packets = [(0, 1), (1, 1), (1, 1)]
        # When
        result = process_packets(S, n, packets)
        # Then
        self.assertEqual(result, [0, 1, 2])

    def test_performance_process_packets(self):
        # Given
        S = 1000
        n = 1000
        packets = [(i, 1) for i in range(1000)]
        # When
        start_time = time.time()
        process_packets(S, n, packets)
        end_time = time.time()
        execution_time = end_time - start_time

        # When
        tracemalloc.start()
        process_packets(S, n, packets)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10**6, 512)

if __name__ == '__main__':
    unittest.main()

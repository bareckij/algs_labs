import unittest
import time
import tracemalloc

class TestBubbleSort(unittest.TestCase):

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            swapped = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def test_bubble_sort(self):
        # Given
        numbers = [5, 3, 8, 4, 2]
        expected_result = [2, 3, 4, 5, 8]

        # When
        sorted_numbers = self.bubble_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_empty_list(self):
        # Given
        numbers = []
        expected_result = []

        # When
        sorted_numbers = self.bubble_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_single_element(self):
        # Given
        numbers = [42]
        expected_result = [42]

        # When
        sorted_numbers = self.bubble_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_sorted_list(self):
        # Given
        numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        # When
        sorted_numbers = self.bubble_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_reverse_sorted_list(self):
        # Given
        numbers = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]

        # When
        sorted_numbers = self.bubble_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_performance(self):
        # Given
        numbers = [i for i in range(1, 101)]
        numbers.reverse()

        # When
        start_time = time.time()
        self.bubble_sort(numbers)
        end_time = time.time()
        execution_time = end_time - start_time

        # Then
        self.assertLess(execution_time, 2)

    def test_memory_usage(self):
        # Given
        numbers = [i for i in range(1, 101)]
        numbers.reverse()

        # When
        tracemalloc.start()
        start_time = time.time()
        self.bubble_sort(numbers)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = end_time - start_time

        # Then
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10**6, 50)

if __name__ == "__main__":
    unittest.main()

import unittest
import time
import tracemalloc


class TestSelectionSort(unittest.TestCase):

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_id = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_id]:
                    min_id = j
            arr[i], arr[min_id] = arr[min_id], arr[i]
        return arr

    def test_selection_sort(self):
        # Given
        numbers = [5, 3, 8, 4, 2]
        expected_result = [2, 3, 4, 5, 8]

        # When
        sorted_numbers = self.selection_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_empty_list(self):
        # Given
        numbers = []
        expected_result = []

        # When
        sorted_numbers = self.selection_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_single_element(self):
        # Given
        numbers = [42]
        expected_result = [42]

        # When
        sorted_numbers = self.selection_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_sorted_list(self):
        # Given
        numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        # When
        sorted_numbers = self.selection_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_reverse_sorted_list(self):
        # Given
        numbers = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]

        # When
        sorted_numbers = self.selection_sort(numbers)

        # Then
        self.assertEqual(sorted_numbers, expected_result)

    def test_performance(self):
        # Given
        numbers = [i for i in range(1, 101)]
        numbers.reverse()

        # When
        start_time = time.time()
        self.selection_sort(numbers)
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
        self.selection_sort(numbers)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = end_time - start_time

        # Then
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 50)



if __name__ == "__main__":
    unittest.main()

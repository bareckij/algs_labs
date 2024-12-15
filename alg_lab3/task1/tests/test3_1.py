import unittest
import time
import tracemalloc
from alg_lab3.task1.src.task1 import randomized_quick_sort
import utils

class TestRandomizedQuickSort(unittest.TestCase):

    def test_sorting(self):
        # Пример 1: Простая сортировка
        test_arr = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        result = randomized_quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertEqual(result, expected, "Тест 1 не пройден!")

        # Пример 2: Пустой список
        test_arr = []
        expected = []
        result = randomized_quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertEqual(result, expected, "Тест 2 не пройден!")

        # Пример 3: Уже отсортированный список
        test_arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = randomized_quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertEqual(result, expected, "Тест 3 не пройден!")

        # Пример 4: Список с одинаковыми элементами
        test_arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        result = randomized_quick_sort(test_arr, 0, len(test_arr) - 1)
        self.assertEqual(result, expected, "Тест 4 не пройден!")

    def test_performance(self):
        # Given
        arr = [i for i in range(100, 0, -1)]  # обратный отсортированный список
        # When measuring time
        start_time = time.time()
        randomized_quick_sort(arr, 0, len(arr) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        # Then
        self.assertLess(execution_time, 2)

        # When measuring memory
        tracemalloc.start()
        randomized_quick_sort(arr, 0, len(arr) - 1)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(peak / 10**6, 256)  # Память должна быть меньше 256 МБ

if __name__ == "__main__":
    unittest.main()

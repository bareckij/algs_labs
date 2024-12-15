import unittest
import time
import tracemalloc
from alg_lab3.task3.src.task import scarecrow_sort
import utils

class TestScarecrowSort(unittest.TestCase):

    def test_scarecrow_sort(self):
        """
        Функция для тестирования алгоритма scarecrow_sort.
        """
        # Пример 1: Обычный случай
        sizes = [2, 1, 3]
        n = 3
        k = 2
        expected = False  # Мы ожидаем False, так как невозможно отсортировать
        result = scarecrow_sort(n, k, sizes)
        self.assertEqual(result, expected, "Тест 1 не пройден!")

        # Пример 2: Пустой список
        sizes = []
        n = 0
        k = 1
        expected = True  # Пустой список всегда отсортирован
        result = scarecrow_sort(n, k, sizes)
        self.assertEqual(result, expected, "Тест 2 не пройден!")

        # Пример 3: Все элементы одинаковые
        sizes = [7, 7, 7, 7]
        n = 4
        k = 2
        expected = True  # Список из одинаковых элементов всегда отсортирован
        result = scarecrow_sort(n, k, sizes)
        self.assertEqual(result, expected, "Тест 3 не пройден!")

        # Пример 4: Сортировка должна быть ложной
        sizes = [3, 1, 4, 2]
        n = 4
        k = 2
        expected = False  # Невозможно отсортировать с разбиением на 2 группы
        result = scarecrow_sort(n, k, sizes)
        self.assertEqual(result, expected, "Тест 4 не пройден!")

        print("Все тесты прошли успешно!")

    def test_performance(self):
        # Тест на производительность
        sizes = [i for i in range(10000, 0, -1)]  # обратный отсортированный список
        n = len(sizes)
        k = 500  # Разбиение на 500 групп
        # Измерение времени
        start_time = time.time()
        scarecrow_sort(n, k, sizes)
        end_time = time.time()
        execution_time = end_time - start_time
        # Проверяем, что выполнение занимает менее 2 секунд
        self.assertLess(execution_time, 2)

        # Измерение памяти
        tracemalloc.start()
        scarecrow_sort(n, k, sizes)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Проверяем, что максимальный расход памяти менее 256 MB
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()

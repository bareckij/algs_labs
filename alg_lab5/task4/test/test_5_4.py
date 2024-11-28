import unittest
import time
import tracemalloc
from alg_lab5.task4.src.task4 import build_min_heap, min_heapify


class TestTask4(unittest.TestCase):
    
    def test_build_min_heap(self):
        # Given: Подготовка данных
        arr = [5, 4, 3, 2, 1]
        
        # When: Выполнение build_min_heap
        swaps = build_min_heap(arr)
        
        # Then: Проверка результата
        # Построенная куча должна быть минимальной
        expected_arr = [1, 2, 3, 5, 4]
        expected_swaps = [(1, 4), (0, 1), (1, 3)]  # Индексы перестановок
        self.assertEqual(arr, expected_arr)
        self.assertEqual(swaps, expected_swaps)

    def test_performance_min_heapify(self):
        # Given: Подготовка данных
        array = [i for i in range(1000, 0, -1)]  # Большой массив для тестирования производительности
        
        # When: Измерение времени выполнения
        start_time = time.time()
        build_min_heap(array)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # When: Измерение потребляемой памяти
        tracemalloc.start()
        build_min_heap(array)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Then: Проверка времени и памяти выполнения
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")
        
        # Убедитесь, что время и память находятся в приемлемых пределах
        self.assertLess(execution_time, 3)  # Пример: время выполнения должно быть меньше 3 секунд
        self.assertLess(peak / 10**6, 512)  # Пример: пиковая память должна быть меньше 512 MB


if __name__ == '__main__':
    unittest.main()

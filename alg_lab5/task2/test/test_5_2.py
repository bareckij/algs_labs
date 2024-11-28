import unittest
import time
import tracemalloc
from alg_lab5.task2.src.task2 import calculate_tree_height  

class TestTask4(unittest.TestCase):
    
    def test_should_calculate_tree_height(self):
        # Given: Подготовка данных
        n = 5
        parents = [-1, 4, 4, 1, 1]
        expected_height = 1  # Ожидаемая высота дерева

        # When: Выполнение функции
        height = calculate_tree_height(n, parents)

        # Then: Проверка результата
        self.assertEqual(height, expected_height)

    def test_performance_calculate_tree_height(self):
        # Given: Подготовка данных
        n = 10000
        parents = [-1] + [i % 100 for i in range(1, n)]  # Строим дерево с большим числом узлов

        # When: Измерение времени выполнения
        start_time = time.time()
        calculate_tree_height(n, parents)
        end_time = time.time()
        execution_time = end_time - start_time

        # When: Измерение потребляемой памяти
        tracemalloc.start()
        calculate_tree_height(n, parents)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then: Проверка времени и памяти выполнения
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        # Убедитесь, что время и память находятся в приемлемых пределах
        self.assertLess(execution_time, 3)  # Пример: время выполнения должно быть меньше 3 секунды
        self.assertLess(peak / 10**6, 512)  # Пример: пиковая память должна быть меньше 512 MB

if __name__ == '__main__':
    unittest.main()

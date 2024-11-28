import unittest
import time
import tracemalloc
from alg_lab5.task3.src.task3 import process_packets  # Импортируем функцию process_packets
import utils 

class TestTask4(unittest.TestCase):
    
    def test_should_process_packets_correctly(self):
        # Given: Подготовка данных
        S = 1
        n = 2
        packets = [(0, 1), (0, 1)]  # Пакеты, где первый можно обработать, второй отбрасывается
        expected_result = [0, -1]  # Ожидаемый результат
        # When: Выполнение функции
        result = process_packets(S, n, packets)

        # Then: Проверка результата
        self.assertEqual(result, expected_result)

    def test_should_process_packets_correctly_multiple(self):
        # Given: Подготовка данных
        S = 2
        n = 3
        packets = [(0, 1), (1, 1), (1, 1)]  # Три пакета, два из которых можно обработать
        expected_result = [0, 1, 2]  # Ожидаемый результат

        # When: Выполнение функции
        result = process_packets(S, n, packets)

        # Then: Проверка результата
        self.assertEqual(result, expected_result)

    def test_performance_process_packets(self):
        # Given: Подготовка данных
        S = 1000  # Размер буфера
        n = 1000  # Количество пакетов
        packets = [(i, 1) for i in range(1000)]  # Массив пакетов, каждый с временем обработки 1

        # When: Измерение времени выполнения
        start_time = time.time()
        process_packets(S, n, packets)
        end_time = time.time()
        execution_time = end_time - start_time

        # When: Измерение потребляемой памяти
        tracemalloc.start()
        process_packets(S, n, packets)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Then: Проверка времени и памяти выполнения
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 10)  # Пример: время выполнения должно быть меньше 10 секунд
        self.assertLess(peak / 10**6, 512)  # Пример: пиковая память должна быть меньше 512 MB

if __name__ == '__main__':
    unittest.main()

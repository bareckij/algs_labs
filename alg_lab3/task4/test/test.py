import time
import tracemalloc
from alg_lab3.task4.src.task4 import count_intervals
import utils

def run_count_intervals():
    """
    Функция для выполнения подсчета отрезков, которые содержат каждую точку,
    с измерением времени и памяти.
    """
    # Начинаем отслеживание памяти
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Чтение данных из файла
    try:
        data = utils.read_data_from_file("alg_lab3/task4/textf/input.txt")
    except Exception as e:
        print(f"Ошибка при чтении данных из файла: {e}")
        return

    # Выполнение алгоритма подсчета интервалов для точек
    try:
        results = count_intervals(data)
    except Exception as e:
        print(f"Ошибка при выполнении функции count_intervals: {e}")
        return

    # Запись результатов в файл
    try:
        utils.write_data_to_file('alg_lab3/task4/textf/output.txt', results)
    except Exception as e:
        print(f"Ошибка при записи данных в файл: {e}")
        return

    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")


if __name__ == "__main__":
    # Запуск функции для выполнения подсчета интервалов
    run_count_intervals()

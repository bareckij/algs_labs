import time
import tracemalloc
from alg_lab3.task5.src.task5 import h_index
import utils

def run_h_index():
    """
    Функция для выполнения вычисления индекса Хирша с измерением времени и памяти.
    """
    # Начинаем отслеживание памяти
    tracemalloc.start()
    t_start = time.perf_counter()

    # Чтение данных из файла
    try:
        arr = utils.read_data_from_file('alg_lab3/task5/textf/input.txt')[0]
    except Exception as e:
        print(f"Ошибка при чтении данных из файла: {e}")
        return

    # Вычисление индекса Хирша
    try:
        result = h_index(arr)
    except Exception as e:
        print(f"Ошибка при вычислении индекса Хирша: {e}")
        return

    # Запись результата в файл
    try:
        utils.write_data_to_file('alg_lab3/task5/textf/output.txt', str(result))
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


def test_h_index():
    """
    Тестирование функции h_index на различных примерах.
    """
    # Пример 1: Стандартный случай
    arr = [3, 0, 6, 1, 5, 2]
    expected = 3
    assert h_index(arr) == expected, "Тест 1 не пройден!"

    # Пример 2: Пустой массив
    arr = []
    expected = 0
    assert h_index(arr) == expected, "Тест 2 не пройден!"

    # Пример 3: Массив из одного элемента
    arr = [1]
    expected = 1
    assert h_index(arr) == expected, "Тест 3 не пройден!"

    # Пример 4: Массив с одинаковыми элементами
    arr = [5, 5, 5, 5, 5]
    expected = 5
    assert h_index(arr) == expected, "Тест 4 не пройден!"

    # Пример 5: Массив с большим количеством одинаковых элементов
    arr = [100] * 1000  # 1000 элементов, все равны 100
    expected = 100  # Индекс Хирша равен 1000
    assert h_index(arr) == expected, "Тест 5 не пройден!"

    # Пример 6: Массив с элементами от 1 до 5
    arr = [1, 2, 3, 4, 5]
    expected = 3
    assert h_index(arr) == expected, "Тест 6 не пройден!"

    # Пример 7: Массив с элементами равными нулю
    arr = [0, 0, 0, 0]
    expected = 0
    assert h_index(arr) == expected, "Тест 7 не пройден!"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    # Запуск функции для вычисления индекса Хирша
    run_h_index()

    # Запуск тестов
    test_h_index()

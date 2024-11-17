import time
import tracemalloc
from alg_lab3.task8.src.task8 import find_k_nearest_points
import utils

def run_find_k_nearest_points():
    """
    Функция для выполнения поиска K ближайших точек с измерением времени и памяти.
    """
    # Начинаем отслеживание памяти
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Чтение данных из файла
    try:
        data = utils.read_data_from_file('alg_lab3/task8/textf/input.txt')
        n = data[0][0]  # Общее количество точек
        k = data[0][1]  # Количество ближайших точек
        points = data[1:n+1]  # Список точек (пропускаем первую строку)
    except Exception as e:
        print(f"Ошибка при чтении данных из файла: {e}")
        return

    # Находим K ближайших точек
    try:
        nearest_points = find_k_nearest_points(points, k)
    except Exception as e:
        print(f"Ошибка при вычислении K ближайших точек: {e}")
        return

    # Форматируем вывод
    output = [f"[{x},{y}]" for x, y in nearest_points]
    
    # Записываем результат в файл
    try:
        utils.write_data_to_file('alg_lab3/task8/textf/output.txt', output)
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


def test_find_k_nearest_points():
    """
    Тестирование функции find_k_nearest_points на различных примерах.
    """
    # Пример 1: Стандартный случай
    points = [(3, 3), (5, -1), (-2, 4)]
    k = 2
    expected = [(3, 3), (-2, 4)]  # Ожидаемые ближайшие точки
    assert find_k_nearest_points(points, k) == expected, "Тест 1 не пройден!"

    # Пример 2: Один набор точек
    points = [(10, 10)]
    k = 1
    expected = [(10, 10)]
    assert find_k_nearest_points(points, k) == expected, "Тест 2 не пройден!"

    # Пример 3: Все точки в одной точке
    points = [(0, 0), (0, 0), (0, 0)]
    k = 2
    expected = [(0, 0), (0, 0)]  # Все точки одинаковые
    assert find_k_nearest_points(points, k) == expected, "Тест 3 не пройден!"

    # Пример 4: Точки с одинаковым расстоянием
    points = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    k = 2
    expected = [(1, 1), (-1, -1)]  # Порядок может быть произвольным, так как расстояния одинаковые
    result = find_k_nearest_points(points, k)
    assert set(result) == set(expected), "Тест 4 не пройден!"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    # Запуск функции для поиска K ближайших точек
    run_find_k_nearest_points()

    # Запуск тестов
    test_find_k_nearest_points()

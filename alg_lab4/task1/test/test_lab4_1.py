import time
import tracemalloc
from alg_lab4.task1.src.task1 import process_commands

def run_process_commands():
    """
    Функция для измерения времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Запуск основной функции
    process_commands('alg_lab4/task1/textf/input.txt', 'alg_lab4/task1/textf/output.txt')
    
    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")

def test_process_commands():
    """
    Функция для тестирования алгоритма обработки команд.
    """
    # Пример 1: Тест с простыми командами для добавления и извлечения элементов
    with open('alg_lab4/task1/textf/input.txt', 'w') as file:
        file.write("5\n+ 1\n+ 2\n- \n+ 3\n- \n")  # 5 команд: добавление 1, 2, извлечение, добавление 3, извлечение
    process_commands('alg_lab4/task1/textf/input.txt', 'alg_lab4/task1/textf/output.txt')

    # Проверка результата
    with open('alg_lab4/task1/textf/output.txt', 'r') as file:
        result = file.read().strip().split('\n')
    expected = ['2', '3']
    assert result == expected, f"Тест 1 не пройден! Ожидалось {expected}, но получено {result}"
def test_empty():
    # Пример 2: Пустой список (нет команд на извлечение)
    with open('alg_lab4/task1/textf/input.txt', 'w') as file:
        file.write("3\n+ 4\n+ 5\n- \n")  # 3 команды: добавление 4, 5 и извлечение
    process_commands('alg_lab4/task1/textf/input.txt', 'alg_lab4/task1/textf/output.txt')

    with open('alg_lab4/task1/textf/output.txt', 'r') as file:
        result = file.read().strip().split('\n')
    expected = ['5']
    assert result == expected, f"Тест 2 не пройден! Ожидалось {expected}, но получено {result}"

def test_only_add():
    # Пример 3: Команды только на добавление
    with open('alg_lab4/task1/textf/input.txt', 'w') as file:
        file.write("3\n+ 6\n+ 7\n+ 8\n")  # 3 команды: добавление 6, 7, 8
    process_commands('alg_lab4/task1/textf/input.txt', 'alg_lab4/task1/textf/output.txt')

    with open('alg_lab4/task1/textf/output.txt', 'r') as file:
        result = file.read().strip().split('\n')
    expected = ['']
    assert result == expected, f"Тест 3 не пройден! Ожидалось {expected}, но получено {result}"


if __name__ == "__main__":

    # Запуск измерений времени и памяти
    run_process_commands()

    # Запуск тестов
    test_empty()
    test_only_add()
    test_process_commands
    print("Все тесты прошли успешно!")


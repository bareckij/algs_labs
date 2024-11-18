import time
import tracemalloc
from alg_lab4.task5.src.task5 import process_commands  

def run_test():
    """
    Функция для измерения времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Запуск основной функции
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    
    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")


def test_stack_operations():
    """
    Функция для тестирования работы с командой стека.
    """

    # Пример 1: Простой случай с несколькими командами
    input_data = """5\npush 1\npush 2\nmax\npop\nmax\n"""
    expected_output = """2\n1\n"""  # Ожидаем, что будет выведено максимальное значение после второго и пятого шага
    with open('alg_lab4/task5/textf/input.txt', 'w') as f:
        f.write(input_data)
    
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    
    # Чтение результата из output.txt
    with open('alg_lab4/task5/textf/output.txt', 'r') as f:
        result = f.read().strip()  # Убираем лишние символы (например, новую строку в конце)
    
    
    assert result == expected_output.strip(), f"Ошибка: ожидалось {expected_output.strip()}, но получено {result}"

def test_empty():
    # Пример 2: Пустой стек
    input_data = """3\npush 5\npop\nmax\n"""
    expected_output = ""  # Ожидаем, что вывод будет пустым, так как стек пуст после pop
    with open('alg_lab4/task5/textf/input.txt', 'w') as f:
        f.write(input_data)
    
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    
    with open('alg_lab4/task5/textf/output.txt', 'r') as f:
        result = f.read().strip()  # Убираем лишние символы
    
    
    assert result == expected_output.strip(), f"Ошибка: ожидалось {expected_output.strip()}, но получено {result}"

def test_maxs():
    # Пример 3: Тест с несколькими запросами max
    input_data = """6\npush 1\npush 3\nmax\npush 2\nmax\npop\nmax\n"""
    expected_output = """3\n3\n"""  # Ожидаем, что всегда будет выводиться максимальное значение
    with open('alg_lab4/task5/textf/input.txt', 'w') as f:
        f.write(input_data)
    
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    
    with open('alg_lab4/task5/textf/output.txt', 'r') as f:
        result = f.read().strip()  # Убираем лишние символы
    
    
    assert result == expected_output.strip(), f"Ошибка: ожидалось {expected_output.strip()}, но получено {result}"

def test_max():
    # Пример 4: Тест с максимальными значениями
    input_data = """4\npush 100000\npush 50000\npush 200000\nmax\n"""
    expected_output = """200000\n"""  # Ожидаем, что максимальное значение будет равно 200000
    with open('alg_lab4/task5/textf/input.txt', 'w') as f:
        f.write(input_data)
    
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    
    with open('alg_lab4/task5/textf/output.txt', 'r') as f:
        result = f.read().strip()  # Убираем лишние символы
    
    
    assert result == expected_output.strip(), f"Ошибка: ожидалось {expected_output.strip()}, но получено {result}"



if __name__ == "__main__":
    run_test()  # Измерение времени и памяти
    test_stack_operations()  # Запуск тестов
    test_empty()
    test_max()
    test_maxs()
    print("Все тесты прошли успешно!")


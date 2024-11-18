import time
import tracemalloc
from alg_lab4.task4.src.task4 import check_brackets
from alg_lab4.task4.src.task4 import process_brackets
def run_check_brackets():
    """
    Функция для измерения времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Запуск основной функции
    process_brackets('alg_lab4/task4/textf/input.txt', 'alg_lab4/task4/textf/output.txt')
    
    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")

def test_check_brackets():
    # Пример 1: правильная последовательность
    input_str = "([])foo(bar[i);]"
    expected = "14"  # Ошибка на 14-й позиции
    result = check_brackets(input_str)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_right():
    # Пример 2: правильная последовательность
    input_str = "([]){[()]}"
    expected = "Success"  # Все скобки корректны
    result = check_brackets(input_str)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_wrong():
    # Пример 3: неправильная последовательность (неправильная закрывающая скобка)
    input_str = "([)]"
    expected = "3"  # Ошибка на 3-й позиции
    result = check_brackets(input_str)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_another():
    # Пример 4: неправильная последовательность (лишняя закрывающая скобка)
    input_str = "([}}"
    expected = "3"  # Ошибка на 3-й позиции
    result = check_brackets(input_str)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"
def test_empty():
    # Пример 5: пустая строка
    input_str = ""
    expected = "Success"  # Пустая строка считается правильной
    result = check_brackets(input_str)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    run_check_brackets()
    test_check_brackets()
    test_empty()
    test_another()
    test_right()
    test_wrong()
    

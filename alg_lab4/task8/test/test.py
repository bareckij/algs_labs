import time
import tracemalloc
from alg_lab4.task8.src.task8 import evaluate_postfix_expression
from alg_lab4.task8.src.task8 import main
import utils
def run_evaluate_postfix_expression():
    """
    Функция для выполнения поиска K ближайших точек с измерением времени и памяти.
    """
    # Начинаем отслеживание памяти
    tracemalloc.start() 
    t_start = time.perf_counter()
    input_file, output_file = 'alg_lab4/task8/textf/input.txt', 'alg_lab4/task8/textf/output.txt'
    n = utils.read_data_from_file(input_file)[0]
    expression = utils.read_data_from_file(input_file)[1].split()
    result = evaluate_postfix_expression(n, expression)
    utils.write_data_to_file(output_file, str(result))
    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")

def test_evaluate_postfix_expression():
    # Простой случай
    expression = ['8', '9', '+']
    expected = 17  # 8 + 9 = 17
    result = evaluate_postfix_expression(len(expression), expression)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_several_operation():
    # Пример с несколькими операциями
    expression = ['8', '9', '+', '1', '7', '-', '*']
    expected = -102  # (8 + 9) * (1 - 7) = 17 * (-6) = -102
    result = evaluate_postfix_expression(len(expression), expression)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_negative_number():
    # Пример с отрицательными числами
    expression = ['5', '3', '-', '10', '2', '-', '*']
    expected = 16  # (5 - 3) * (10 - 2) = 2 * 8 = 16
    result = evaluate_postfix_expression(len(expression), expression)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_one_number():
    # Пример с одним числом (тест на базовый случай)
    expression = ['42']
    expected = 42  # Один операнд - сам результат
    result = evaluate_postfix_expression(len(expression), expression)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_more_harder():
    # Пример с более сложным выражением
    expression = ['2', '3', '4', '+', '*', '5', '+']
    expected = 19  # 2 * (3 + 4) + 5 = 2 * 7 + 5 = 14 + 5 = 19
    result = evaluate_postfix_expression(len(expression), expression)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

# Для проверки тестов
if __name__ == "__main__":
    run_evaluate_postfix_expression()
    test_evaluate_postfix_expression()
    test_several_operation()
    test_more_harder()
    test_negative_number()
    test_one_number()
    print('All test passed')

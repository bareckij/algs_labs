from alg_lab4.task2.src.task import process_commands

def run_all_tests():
    # Тест 1: Простая проверка на добавление и извлечение нескольких элементов.
    commands = [
        ["+", 1],
        ["+", 10],
        ["-"],
        ["-"],
    ]
    expected = [1, 10]
    result = process_commands(commands)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"
def test_empty():
    # Тест 2: Проверка извлечения из пустой очереди (не должно быть извлечений).
    commands = [
        ["+", 5],
        ["-",],
        ["-",],  # Не должно быть извлечений
    ]
    expected = [5]
    result = process_commands(commands)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_not_extract():
    # Тест 3: Проверка, когда только добавляются элементы и не извлекаются.
    commands = [
        ["+", 1],
        ["+", 2],
        ["+", 3],
    ]
    expected = []
    result = process_commands(commands)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_delete():
    # Тест 4: Проверка на полное удаление элементов (все извлекаются).
    commands = [
        ["+", 1],
        ["+", 2],
        ["+", 3],
        ["-",],  # Извлекаем 1
        ["-",],  # Извлекаем 2
        ["-",],  # Извлекаем 3
    ]
    expected = [1, 2, 3]
    result = process_commands(commands)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_add_extract():
    # Тест 5: Смешанные операции добавления и извлечения.
    commands = [
        ["+", 1],
        ["+", 10],
        ["-",],  # Извлекаем 1
        ["+", 20],
        ["-",],  # Извлекаем 10
        ["-",],  # Извлекаем 20
    ]
    expected = [1, 10, 20]
    result = process_commands(commands)
    assert result == expected, f"Ошибка: ожидалось {expected}, но получено {result}"

def test_a_lot():
    # Тест 6: Большое количество команд.
    commands = [["+", i] for i in range(1, 10001)] + [["-"] for _ in range(10000)]
    expected = list(range(1, 10001))
    result = process_commands(commands)
    assert result == expected, f"Ошибка: результат не совпадает для большого входа"


if __name__ == "__main__":
    run_all_tests()
    test_a_lot()
    test_add_extract()
    test_delete()
    test_empty()
    test_not_extract()
    print("Все тесты прошли успешно!")

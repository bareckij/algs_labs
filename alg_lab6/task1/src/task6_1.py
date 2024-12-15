def process_operations(n, operations):
    # Множество для хранения элементов
    s = set()

    # Результат выполнения операций
    result = []

    # Обрабатываем каждую операцию
    for operation in operations:
        parts = operation.strip().split()
        cmd = parts[0]
        x = int(parts[1])

        if cmd == 'A':
            s.add(x)  # добавляем элемент в множество (если его нет)
        elif cmd == 'D':
            s.discard(x)  # удаляем элемент из множества (если есть, иначе ничего не делаем)
        elif cmd == '?':
            if x in s:
                result.append('Y')
            else:
                result.append('N')

    return result

# Пример списка операций
operations = [
    "A 2",
    "A 5",
    "A 3",
    "? 2",
    "? 4",
    "A 2",
    "D 2",
    "? 2"
]

# Число операций
n = len(operations)  # число операций, которое всегда равно длине списка

# Вызов функции
result = process_operations(n, operations)

# Вывод результата
for res in result:
    print(res)

import utils

def process_commands(input_file, output_file):
    # Чтение входных данных
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())  # Читаем количество команд
        commands = [file.readline().strip() for _ in range(n)]  # Читаем все команды

    stack = []  # Основной стек
    max_stack = []  # Стек для максимальных значений
    results = []  # Список для результатов команд max

    for command in commands:
        if command.startswith("push"):
            # Команда push V
            _, V = command.split()
            V = int(V)
            stack.append(V)
            # Если max_stack пуст, добавляем V, иначе добавляем максимум из V и текущего максимума
            if max_stack:
                max_stack.append(max(V, max_stack[-1]))
            else:
                max_stack.append(V)
        
        elif command == "pop":
            # Команда pop
            if stack:
                stack.pop()
                max_stack.pop()
        
        elif command == "max":
            # Команда max
            if max_stack:
                results.append(str(max_stack[-1]))  # Добавляем максимальное значение

    # Запись результатов в файл
    with open(output_file, 'w') as file:
        file.write("\n".join(results) + "\n")

# Запуск основной функции
if __name__ == "__main__":
    print('Lab4/task5')
    process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
    print(utils.read_data_from_file('alg_lab4/task5/textf/output.txt'))


def process_commands(input_file, output_file):
    # Открываем файлы для чтения и записи(*)
    with open(input_file, 'r') as file:
        # Читаем количество команд
        M = int(file.readline().strip())
        
        # Стек для хранения данных
        stack = []
        
        # Список для вывода результатов извлечений
        result = []
        
        # Обрабатываем все команды
        for _ in range(M):
            command = file.readline().strip()
            
            # Обработка команды добавления в стек
            if command[0] == '+':
                _, N = command.split()
                stack.append(int(N))
            
            # Обработка команды извлечения из стека
            elif command[0] == '-':
                result.append(stack.pop())
        
    # Запись результата в файл
    with open(output_file, 'w') as file:
        file.write('\n'.join(map(str, result)) + '\n')


# Запуск основной функции
if __name__ == "__main__":
    process_commands('alg_lab4/task1/textf/input.txt', 'alg_lab4/task1/textf/output.txt')


from collections import deque
import utils
def process_commands(commands):
    queue = deque()  # Используем deque для очереди
    result = []

    for command in commands:
        if command[0] == "+":
            # Добавляем элемент в очередь
            queue.append(command[1])
        elif command[0] == "-":
            # Извлекаем элемент из очереди, если она не пуста
            if queue:
                result.append(queue.popleft())  # Используем popleft для удаления с начала
            else:
                # Очередь пуста, можно обработать эту ошибку (если требуется)
                continue
        # Если команда запроса на извлечение минимального элемента, ничего не делаем
        # если она не входит в список команд
    return result

def read_input(file_path):
    m = utils.read_data_from_file(file_path)[0]
    commands = []
    for i in range(m):
        command = utils.read_data_from_file(file_path)[i+1]
        command = command.split()
        if command[0] == "+":
            commands.append([command[0], int(command[1])])
        else:
            commands.append([command[0]])
    return commands

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        f.write("\n".join(map(str, results)) + "\n")

def main(input_file, output_file):
    commands = read_input(input_file)
    results = process_commands(commands)
    write_output(output_file, results)

if __name__ == "__main__":
    main('alg_lab4/task2/textf/input.txt', 'alg_lab4/task2/textf/output.txt')

import utils

def check_brackets(S):
    # Стек для хранения открывающих скобок и их индексов
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for i, char in enumerate(S):
        if char in '({[':
            # Добавляем открывающую скобку в стек с индексом (индексация с 1)
            stack.append((char, i + 1))
        elif char in ')}]':
            if not stack:
                # Стек пуст, но есть закрывающая скобка - ошибка
                return str(i + 1)
            top, top_index = stack.pop()
            if matching_bracket[char] != top:
                # Несоответствие закрывающей скобки и открывающей - ошибка
                return str(i + 1)
    
    # Если после обработки строки стек не пуст, то есть открытая скобка без пары
    if stack:
        _, top_index = stack[0]  # Индекс первой не закрытой открывающей скобки
        return str(top_index)
    
    return "Success"


def process_brackets(input_file, output_file):
    S = utils.read_data_from_file(input_file)
    # Проверяем правильность скобок в строке
    result = check_brackets(S)
    
    # Записываем результат в файл
    with open(output_file, 'w') as f:
        f.write(result + "\n")


if __name__ == "__main__":
    print('Lab4/task4') 
    process_brackets('alg_lab4/task4/textf/input.txt', 'alg_lab4/task4/textf/output.txt')
    print(utils.read_data_from_file('alg_lab4/task4/textf/output.txt'))

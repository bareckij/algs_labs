import utils

def evaluate_postfix_expression(n, expression):
    stack = []
    
    # Обрабатываем каждый элемент в выражении
    for token in expression:
        if token.isdigit():  # Если элемент - число, добавляем его в стек
            stack.append(int(token))
        else:  # Если элемент - операция, извлекаем два операнда и применяем операцию
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    # В стеке останется только один элемент - результат
    return stack[0]

def main(input_file, output_file):
    n = utils.read_data_from_file(input_file)[0]
    expression = utils.read_data_from_file(input_file)[1].split()
    result = evaluate_postfix_expression(n, expression)
    utils.write_data_to_file(output_file, str(result))

if __name__ == "__main__":
    main('alg_lab4/task8/textf/input.txt', 'alg_lab4/task8/textf/output.txt')
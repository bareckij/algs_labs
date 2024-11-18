from collections import deque
import utils 
def sliding_window_maximum(arr, n, m):
    # deque для хранения индексов
    deq = deque()
    result = []
    
    for i in range(n):
        # Удаляем индексы, которые выходят за пределы текущего окна
        while deq and deq[0] <= i - m:
            deq.popleft()
        
        # Удаляем элементы из deque, которые меньше текущего элемента
        while deq and arr[deq[-1]] <= arr[i]:
            deq.pop()
        
        # Добавляем текущий элемент в deque
        deq.append(i)
        
        # Если окно заполнено, добавляем максимальный элемент текущего окна
        if i >= m - 1:
            result.append(arr[deq[0]])  # максимальный элемент - это элемент на позиции deq[0]
    
    return result

def process_commands():
    n, arr, m = utils.read_data_from_file('alg_lab4/task7/textf/input.txt')
    # Получение результата
    result = sliding_window_maximum(arr, n, m)
    
    # Запись результата в output_file
    utils.write_data_to_file('alg_lab4/task7/textf/output.txt', result)
if __name__ == "__main__":
    print('Lab4/task7')
    process_commands()
    print(utils.read_data_from_file('alg_lab4/task7/textf/output.txt'))

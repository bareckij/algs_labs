import time
import tracemalloc
from task10.src.task10 import merge_sort
 
tracemalloc.start()
t_start = time.perf_counter()
  
with open('task1/textf/input_without.txt', 'r') as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

merge_sort(arr, 0, n-1)

with open('task1/textf/output_without.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))
print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
import time
import tracemalloc
from task7.src.task7 import find_max_subarray
 
tracemalloc.start()
t_start = time.perf_counter()
  

with open('task7/textf/input.txt', 'r') as f:
    arr = list(map(int, f.readline().split()))

max_sum = find_max_subarray(arr)

with open('task7/textf/output.txt', 'w') as f:
    f.write(str(max_sum))
print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
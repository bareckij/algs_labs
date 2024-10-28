import time
import tracemalloc
from alg_lab2.task5.src.task5 import is_majority_element
 
tracemalloc.start()
t_start = time.perf_counter()
  
with open('alg_lab2/task5/textf/input.txt', 'r') as f:
    n = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))

result = is_majority_element(A)

with open('alg_lab2/task5/textf/output.txt', 'w') as f:
    f.write(str(result))

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
import time
import tracemalloc
from task4.src.task4 import binary_search
 
tracemalloc.start()
t_start = time.perf_counter()

with open('task4/textf/input.txt', 'r') as file:
    n = int(file.readline().split()[0])
    arr = list(map(int, file.readline().split()))
    k = int(file.readline().split()[0])
    search_nums = list(map(int, file.readline().split()))

results = []
for num in search_nums:
    result = binary_search(arr, num)
    results.append(result)  
with open('task4/textf/output.txt', 'w') as file:
    file.write(' '.join(map(str, results)))

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
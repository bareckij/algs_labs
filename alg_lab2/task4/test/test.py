import time
import tracemalloc
from task4.src.task4 import binary_search
import utils
tracemalloc.start()
t_start = time.perf_counter()

n, arr, k, search_nums = utils.read_data_from_file('task4/textf/input.txt')

results = []
for num in search_nums:
    result = binary_search(arr, num)
    results.append(result)  
utils.write_data_to_file('task4/textf/input.txt', results)

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
import time
import tracemalloc
from task10.src.task10 import merge_sort
import utils 

tracemalloc.start()
t_start = time.perf_counter()
  

n, arr, k, b_arr = utils.read_data_from_file('task1/textf/input_without.txt')
data = merge_sort(arr, 0, n-1)

utils.write_data_to_file('task1/textf/output_without.txt', data)

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
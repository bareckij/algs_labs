import time
import tracemalloc
from alg_lab2.task1.src.task1 import merge_sort
import utils

tracemalloc.start()
t_start = time.perf_counter()

n= utils.read_data_from_file('alg_lab2/task1/textf/input.txt')[0]
arr= utils.read_data_from_file('alg_lab2/task1/textf/input.txt')[1]
data=merge_sort(arr, 0, n-1)

utils.write_data_to_file('alg_lab2/task1/textf/output.txt', data)


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
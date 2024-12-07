import time
import tracemalloc
from alg_lab2.task7.src.task7 import find_max_subarray
import utils

tracemalloc.start()
t_start = time.perf_counter()

arr = utils.read_data_from_file('alg_lab2/task7/textf/input.txt')

max_subarray = find_max_subarray(arr[0])

utils.write_data_to_file('alg_lab2/task7/textf/output.txt', max_subarray)

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
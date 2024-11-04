import time
import tracemalloc
from alg_lab3.task3.src.task import scarecrow_sort
import utils

tracemalloc.start() 
t_start = time.perf_counter()

n, k= utils.read_data_from_file('alg_lab3/task3/textf/input.txt')[0]
sizes = utils.read_data_from_file('alg_lab3/task3/textf/input.txt')[1]

if scarecrow_sort(n, k, sizes):
    result = "Yes"
else:
    result = "No"

utils.write_data_to_file('alg_lab3/task3/textf/output.txt', result)


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
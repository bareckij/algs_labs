import time
import tracemalloc
from alg_lab2.task5.src.task5 import is_majority_element
import utils
tracemalloc.start()
t_start = time.perf_counter()
  

n, arr= utils.read_data_from_file('alg_lab2/task5/textf/input.txt')

result = is_majority_element(arr)

utils.write_data_to_file('alg_lab2/task5/textf/output.txt', str(result))
print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
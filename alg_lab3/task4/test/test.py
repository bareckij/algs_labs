import time
import tracemalloc
from alg_lab3.task4.src.task4 import count_intervals
import utils

tracemalloc.start() 
t_start = time.perf_counter()

data = utils.read_data_from_file("alg_lab3/task4/textf/input.txt")


results = count_intervals(data)


utils.write_data_to_file('alg_lab3/task4/textf/output.txt', results)


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
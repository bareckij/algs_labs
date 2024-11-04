import time
import tracemalloc
from alg_lab3.task6.src.task import sum_of_every_tenth_product
import utils

tracemalloc.start() 
t_start = time.perf_counter()

data = utils.read_data_from_file("alg_lab3/task6/textf/input.txt")


results = sum_of_every_tenth_product(data[1], data[2])

utils.write_data_to_file('alg_lab3/task6/textf/output.txt', [results])


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
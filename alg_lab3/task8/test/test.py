import time
import tracemalloc
from alg_lab3.task8.src.task8 import find_k_closest_points
import utils
tracemalloc.start()
t_start = time.perf_counter()
n, array, k, _ = utils.read_data_from_file('alg_lab3/task8/textf/input.txt')
points = [(array[i], array[i + 1]) for i in range(0, len(array), 2)]
    
    # Находим K ближайших точек
closest_points = find_k_closest_points(n, k, points)
    
    # Форматируем вывод
result = [f'({x}, {y})' for x, y in closest_points]
utils.write_data_to_file('alg_lab3/task8/textf/output.txt', result)

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
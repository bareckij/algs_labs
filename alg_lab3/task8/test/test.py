import time
import tracemalloc
from alg_lab3.task8.src.task8 import find_k_nearest_points
import utils
tracemalloc.start()
t_start = time.perf_counter()

def main():
    # Читаем данные из файла
    data = utils.read_data_from_file('alg_lab3/task8/textf/input.txt')
    
    n = data[0][0]  # Общее количество точек
    k = data[0][1]  # Количество ближайших точек
    points = data[1:n+1]  # Список точек (пропускаем первую строку)

    # Находим K ближайших точек
    nearest_points = find_k_nearest_points(points, k)

    # Форматируем вывод
    output = [f"[{x},{y}]" for x, y in nearest_points]
    
    # Записываем результат в файл
    utils.write_data_to_file('alg_lab3/task8/textf/output.txt', output)

if __name__ == "__main__":
    main()

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
import utils

def find_k_nearest_points(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

if __name__ == "__main__":
    data = utils.read_data_from_file('alg_lab3/task8/textf/input.txt')
    n = data[0][0]  # Общее количество точек
    k = data[0][1]  # Количество ближайших точек
    points = data[1:n+1]  # Список точек (пропускаем первую строку)
    nearest_points = find_k_nearest_points(points, k)
    output = [f"[{x},{y}]" for x, y in nearest_points]
    utils.write_data_to_file('alg_lab3/task8/textf/output.txt', output)


import utils

def calculate_tree_height(n, parents):
    # Строим список дочерних узлов для каждого узла
    children = [[] for _ in range(n)]
    
    root = -1
    
    # Заполняем список детей
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child  # Находим корень
        else:
            children[parent].append(child)

    # Функция для вычисления высоты дерева через обход в глубину
    def dfs(node):
        if not children[node]:  # Если у узла нет детей, его высота 1
            return 1
        max_height = 0
        for child in children[node]:
            max_height = max(max_height, dfs(child))
        return max_height + 1
    
    # Вычисляем высоту дерева от корня
    return dfs(root)

if __name__ == "__main__":
    n = utils.read_data_from_file('alg_lab5/task2/textf/input.txt')[0]
    parent = utils.read_data_from_file('alg_lab5/task2/textf/input.txt')[1]
    result = calculate_tree_height(n, parent)
    utils.write_data_to_file('alg_lab5/task2/textf/output.txt', str(result))
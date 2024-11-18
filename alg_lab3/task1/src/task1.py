import random
import utils

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1) 


def randomized_quick_sort(arr, low, high):
    if len(arr) == 1:
        return  
    if low < high:
        pi = random.randint(low, high)
        arr[pi], arr[high] = arr[high], arr[pi]
        pi = partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)
    return arr

if __name__ == "__main__":
    n, arr = utils.read_data_from_file('alg_lab3/task1/textf/input.txt')
    sorted_arr = randomized_quick_sort(arr, 0, n - 1)
    utils.write_data_to_file('alg_lab3/task1/textf/output.txt', sorted_arr)
    print('Задание 1\n', utils.read_data_from_file('alg_lab3/task1/textf/output.txt'))

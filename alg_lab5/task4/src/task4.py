import utils

def min_heapify(arr, n, i, swaps):
    smallest = i  
    left = 2 * i + 1 
    right = 2 * i + 2  

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))  # Сохраняем перестановку
        min_heapify(arr, n, smallest, swaps)

def build_min_heap(arr):
    n = len(arr)
    swaps = [] 
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i, swaps)
    return swaps

if __name__ == "__main__":
    n = utils.read_data_from_file('alg_lab5/task4/textf/input.txt')[0]
    arr = utils.read_data_from_file('alg_lab5/task4/textf/input.txt')[1]
    swaps = build_min_heap(arr)    
    utils.write_data_to_file('alg_lab5/task4/textf/output.txt', (len(swaps),'\n',swaps))
    print('lab5/task2')
    print(swaps)
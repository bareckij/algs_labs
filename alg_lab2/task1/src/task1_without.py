import time
import tracemalloc
import utils

def merge_without_inf(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]  

            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_without(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_without(arr, left, mid)
        merge_sort_without(arr, mid + 1, right)
        merge_without_inf(arr, left, mid, right)
    return arr


tracemalloc.start()
t_start = time.perf_counter()

n= utils.read_data_from_file('alg_lab2/task1/textf/input_without.txt')[0]
arr= utils.read_data_from_file('alg_lab2/task1/textf/input_without.txt')[1]
data=merge_sort_without(arr, 0, n-1)

utils.write_data_to_file('alg_lab2/task1/textf/output_without.txt', data)


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
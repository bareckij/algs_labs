import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()

input = open('alg_lab1/task1/txtf/input.txt')
n = int(input.readline().split()[0])    
nums = list(map(int, input.readlines()[1].split()))
new_nums = [num for num in nums if abs(num) <= abs(10**9)][:n]

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
open('alg_lab1/task1/txtf/output.txt', 'w').write(' '.join(map(str, insertion_sort(new_nums))))

print("Time: %s second " % (time.perf_counter() - t_start))
print("Memory used:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "MB" )
tracemalloc.stop()

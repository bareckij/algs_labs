import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()

input = open('alg_lab1/task6/txtf/input.txt')
n = int(input.readline().split()[0])    
nums = list(map(int, input.readlines()[1].split()))
new_nums = [num for num in nums if abs(num) <= abs(10**9)][:n]

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

open('alg_lab1/task6/txtf/output.txt', 'w').write(' '.join(map(str, bubble_sort(new_nums))))

print("Time: %s second " % (time.perf_counter() - t_start))
print("Memory used:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "MB" )
tracemalloc.stop()

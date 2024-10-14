import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()

input = open('task5/txtf/input.txt')
n = int(input.readline().split()[0])    
nums = list(map(int, input.readlines()[1].split()))
new_nums = [num for num in nums if abs(num) <= abs(109)][:n]

def selection_sort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id], arr[i]
    return arr 

open('task5/txtf/output.txt', 'w').write(' '.join(map(str, selection_sort(new_nums))))

print("Time: %s second " % (time.perf_counter() - t_start))
print("Memory used:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "MB" )
tracemalloc.stop()
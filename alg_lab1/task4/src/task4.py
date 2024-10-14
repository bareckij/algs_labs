import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()

input = open('task4/src/input.txt')
V = int(input.readlines()[1])
numbers = list(map(int,open('task4/src/input.txt').readline().split()))
if -10**3<=V<=10**3 and 0 <= numbers[-1] <=10*3:
    def linear_search(arr, target):
        count = 0
        indexes = [] 
        for i, e in enumerate(arr):
            if e == target:
                count+=1        
                indexes.append(i)
        return indexes, count     
    output_indexes = ' '.join(str(i) for i in linear_search(numbers, V)[0])
    output_count = str(linear_search(numbers, V)[1])
    open('task4/src/output.txt', 'w').write(f'The number {V} occurs {output_count} on the indexes {output_indexes} in list {open('task4/src/input.txt').readline()}')
else: 
    print('write other numbers')

print("Time: %s second " % (time.perf_counter() - t_start))
print("Memory used:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "MB" )
tracemalloc.stop()

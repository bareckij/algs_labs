import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()

input = open('alg_lab1/task9/txtf/input.txt').readline().strip().split()
first_number_from_list = list(map(int, input[0]))
second_number_from_list = list(map(int, input[1]))

def add_two_binary(first_number, second_number):
    n = max(len(first_number), len(second_number))

    first_number = [0] * (n - len(first_number)) + first_number
    second_number = [0] * (n - len(second_number)) + second_number

    result = [0] * (n+1)
    carry = 0
    for i in range(n-1, -1, -1):
        temp_sum = first_number[i] + second_number[i] + carry
        result[i+1] = temp_sum % 2
        carry = temp_sum // 2
    result[0] = carry
    return result

open('alg_lab1/task9/txtf/output.txt', 'w').write(''.join(map(str, add_two_binary(first_number_from_list, second_number_from_list))).lstrip('0') or '0')

print("Time: %s second " % (time.perf_counter() - t_start))
print("Memory used:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "MB" )
tracemalloc.stop()

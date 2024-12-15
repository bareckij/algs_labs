import math
import utils

def is_fibonacci(n):
    x = int(n)
    
    def is_perfect_square(num):
        s = int(math.isqrt(num))
        return s * s == num
    
    return is_perfect_square(5 * x * x + 4) or is_perfect_square(5 * x * x - 4)

def process_fibonacci_check(queries):
    results = []
    for query in queries:
        if is_fibonacci(query):
            results.append("Yes")
        else:
            results.append("No")
    return results

if __name__ == '__main__':
    data = utils.read_data_from_file('alg_lab6/task6/textf/input.txt')
    N = int(data[0])
    queries = data[1:N+1]
    res = process_fibonacci_check(queries)
    utils.write_data_to_file('alg_lab6/task6/textf/output.txt', res)

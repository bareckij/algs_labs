def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
with open('alg_lab2/task4/textf/input.txt', 'r') as f:
    n = int(f.readline().split()[0])
    arr = list(map(int, f.readline().split()))
    k = int(f.readline().split()[0])
    search_nums = list(map(int, f.readline().split()))

results = []
for num in search_nums:
    result = binary_search(arr, num)
    results.append(result)
with open('alg_lab2/task4/textf/output.txt', 'w') as f:
    f.write(' '.join(map(str, results)))
input = open('task3/input.txt')
n = int(input.readline().split()[0])    
nums = list(map(int, input.readlines()[1].split()))
new_nums = [num for num in nums if abs(num) <= abs(109)][:n]


def insertion_sort(arr):
    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            swap(j, j+1)
            j -=1
    return arr


open('task3/output.txt', 'w').write(' '.join(map(str, insertion_sort(new_nums))))
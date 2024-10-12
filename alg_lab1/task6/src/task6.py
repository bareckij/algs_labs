input = open('task6/input.txt')
n = int(input.readline().split()[0])    
nums = list(map(int, input.readlines()[1].split()))
new_nums = [num for num in nums if abs(num) <= abs(109)][:n]

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

open('task6/output.txt', 'w').write(' '.join(map(str, bubble_sort(new_nums))))
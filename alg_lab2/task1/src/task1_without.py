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


with open('alg_lab2/task1/textf/input_without.txt', 'r') as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

merge_sort_without(arr, 0, n-1)

with open('alg_lab2/task1/textf/output_without.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))
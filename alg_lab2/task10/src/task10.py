def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0
    k = left
    while k <= right:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
def merge_sort(arr, left, right):
    if left < right:  # Base case: stop recursion when sub-array has one element
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        if arr[mid] > arr[mid + 1]:  # Check for merge only if necessary
            merge(arr, left, mid, right)


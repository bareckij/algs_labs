def count_occurrences(array, target, left, right):
    count = 0
    for i in range(left, right + 1):
        if array[i] == target:
            count += 1
    return count

def find_majority_candidate(array, left, right):
    if left == right:
        return array[left]
    
    mid = (left + right) // 2
    
    left_candidate = find_majority_candidate(array, left, mid)
    right_candidate = find_majority_candidate(array, mid + 1, right)
    
    if left_candidate == right_candidate:
        return left_candidate
    
    left_count = count_occurrences(array, left_candidate, left, right)
    right_count = count_occurrences(array, right_candidate, left, right)
    
    if left_count > right_count:
        return left_candidate
    return right_candidate

def is_majority_element(array):
    n = len(array)
    candidate = find_majority_candidate(array, 0, n - 1)
    
    if candidate is not None:
        total_count = count_occurrences(array, candidate, 0, n - 1)
        if total_count > n // 2:
            return 1  
    return 0   
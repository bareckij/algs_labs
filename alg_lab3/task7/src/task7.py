def find_max_subarray(arr):
    max_sum = current_sum = 0
    start = end = 0
    max_subarray = []
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            start = start_index
            end = i
            max_subarray = arr[start:end+1]  # Сохраняем текущий подмассив
        if current_sum < 0:
            current_sum = 0
            start_index = i + 1
    
    return max_subarray

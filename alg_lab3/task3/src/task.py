def scarecrow_sort(n, k, sizes):
    groups = [[] for _ in range(k)]
    
    for i in range(n):
        groups[i % k].append(sizes[i])
    
    for group in groups:
        group.sort()
    
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])
    
    return sorted_sizes == sorted(sizes)
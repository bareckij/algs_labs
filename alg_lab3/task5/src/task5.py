def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c > i:
            h = i + 1
        else:
            break
    return h

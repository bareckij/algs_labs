input = open('task4/input.txt')
V = int(input.readlines()[1])
numbers = list(map(int,open('task4/input.txt').readline().split()))
if -10**3<=V<=10**3 and 0 <= numbers[-1] <=10*3:
    def linear_search(arr, target):
        count = 0
        indexes = [] 
        for i, e in enumerate(arr):
            if e == target:
                count+=1        
                indexes.append(i)
        return indexes, count     
    output_indexes = ' '.join(str(i) for i in linear_search(numbers, V)[0])
    output_count = str(linear_search(numbers, V)[1])
    open('task4/output.txt', 'w').write(f'The number {V} occurs {output_count} on the indexes {output_indexes} in list {open('task4/input.txt').readline()}')
else: 
    print('write other numbers')
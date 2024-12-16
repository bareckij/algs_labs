from utils import read_data_from_file, write_data_to_file

def process_operations(n, operations):
    s = set()

    result = []

    for operation in operations:
        parts = operation.strip().split()
        cmd = parts[0]
        x = int(parts[1])

        if cmd == 'A':
            s.add(x)  
        elif cmd == 'D':
            s.discard(x)  
        elif cmd == '?':
            if x in s:
                result.append('Y')
            else:
                result.append('N')

    return result

if __name__ =='__main__':
    data = read_data_from_file('alg_lab6/task1/textf/input.txt')
    n = data[0]
    operations = data[1:]
    result = process_operations(n, operations)
    write_data_to_file('alg_lab6/task1/textf/output.txt', result)
    print('lab6/task1')
    print(result)

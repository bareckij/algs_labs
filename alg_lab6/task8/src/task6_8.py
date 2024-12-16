from utils import read_data_from_file, write_data_to_file

def process_operations(N, X, A, B, AC, BC, AD, BD):
    table = set()

    for _ in range(N):
        if X in table:
            A = (A + AC) % 103
            B = (B + BC) % 10**15
        else:
            table.add(X)
            A = (A + AD) % 103
            B = (B + BD) % 10**15
        
        X = (X * A + B) % 10**15

    return X, A, B

if __name__ == '__main__':
    data = read_data_from_file('alg_lab6/task8/textf/input.txt')
    N, X, A, B = data[0]
    AC, BC, AD, BD = data[1]
    X, A, B = process_operations(N, X, A, B, AC, BC, AD, BD)
    write_data_to_file('alg_lab6/task8/textf/output.txt', [X, A, B])
    print('lab6/task8')
    print([X, A, B])

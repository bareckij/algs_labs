def read_data_from_file(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        first_elements = list(map(int, first_line.split()))
        
        if len(first_elements) == 1:
            n = first_elements[0]
            array = list(map(int, f.readline().strip().split()))
            k = 0
            b_array = []
        
        else:
            array = first_elements
            n = len(array)
            
            second_line = f.readline().strip()
            if second_line.isdigit():
                n = int(second_line)
                
            third_line = f.readline().strip()
            if third_line.isdigit():
                k = int(third_line)
                b_array = list(map(int, f.readline().strip().split()))
            else:
                k = 0
                b_array = []

        return n, array, k, b_array

def write_data_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(' '.join(list(map(str, data))))


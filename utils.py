
def read_data_from_file(file_path: str):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Убираем пробелы и проверяем длину
            line = line.strip()
            if len(line.split()) == 1:
                data.append(int(line))
            else:
                data.append(list(map(int, line.split())))
    return data

def write_data_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(" ".join(map(str, data)))


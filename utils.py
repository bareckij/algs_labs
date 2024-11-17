def read_data_from_file(file_path: str):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line.split()) == 1:
                try:
                    data.append(int(line))
                except ValueError:
                    data.append(line)

            else:
                try:
                    data.append(list(map(int, line.split())))
                except ValueError:
                    data.append(line)

    return data

def write_data_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(" ".join(map(str, data)))


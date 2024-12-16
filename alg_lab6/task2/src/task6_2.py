from utils import read_data_from_file, write_data_to_file

def process_phonebook_queries(n, queries):
    phonebook = {}

    result = []

    for query in queries:
        parts = query.split()
        command = parts[0]

        if command == "add":
            number = parts[1]
            name = parts[2]
            phonebook[number] = name  

        elif command == "del":
            number = parts[1]
            if number in phonebook:
                del phonebook[number]  

        elif command == "find":
            number = parts[1]
            if number in phonebook:
                result.append(phonebook[number])  
            else:
                result.append("not found")  

    return result

if __name__ == '__main__':
    data = read_data_from_file('alg_lab6/task2/textf/input.txt')
    n = data[0]
    queries = data[1:]    
    result = process_phonebook_queries(n, queries)
    write_data_to_file('alg_lab6/task2/textf/output.txt', result)
    print('lab6/task1')
    print(result)
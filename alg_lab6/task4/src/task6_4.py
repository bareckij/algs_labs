import utils

class AssociativeArray:
    def __init__(self):
        self.hash_map = {}
        self.keys_order = []
        self.key_position = {}

    def get(self, x):
        if x in self.hash_map:
            return self.hash_map[x]
        return "<none>"

    def prev(self, x):
        if x in self.key_position:
            pos = self.key_position[x]
            if pos > 0:
                return self.hash_map[self.keys_order[pos - 1]]
        return "<none>"

    def next(self, x):
        if x in self.key_position:
            pos = self.key_position[x]
            if pos < len(self.keys_order) - 1:
                return self.hash_map[self.keys_order[pos + 1]]
        return "<none>"

    def put(self, x, y):
        if x not in self.hash_map:
            self.keys_order.append(x)
            self.key_position[x] = len(self.keys_order) - 1
        self.hash_map[x] = y

    def delete(self, x):
        if x in self.hash_map:
            idx = self.key_position.pop(x)
            del self.hash_map[x]
            self.keys_order.pop(idx)
            for i in range(idx, len(self.keys_order)):
                self.key_position[self.keys_order[i]] = i

def process_operations(n, operations):
    arr = AssociativeArray()
    result = []

    for op in operations:
        parts = op.split()
        command = parts[0]
        
        if command == "get":
            result.append(arr.get(parts[1]))
        elif command == "prev":
            result.append(arr.prev(parts[1]))
        elif command == "next":
            result.append(arr.next(parts[1]))
        elif command == "put":
            arr.put(parts[1], parts[2])
        elif command == "delete":
            arr.delete(parts[1])

    return result

if __name__ == '__main__':
    data = utils.read_data_from_file('alg_lab6/task4/textf/input.txt')
    n = int(data[0])
    operations = data[1:]
    result = process_operations(n, operations)
    utils.write_data_to_file('alg_lab6/task4/textf/output.txt', result)
    print('lab6/task1')
    print(result)
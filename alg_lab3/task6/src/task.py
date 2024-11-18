from alg_lab3.task1.src.task1 import randomized_quick_sort 
import utils 
def sum_of_every_tenth_product(array_a, array_b):
    product_list = []
    for b in array_b:
        for a in array_a:
            product_list.append(a * b)
    
    randomized_quick_sort(product_list, 0, len(product_list) - 1)
    sum_tenth_elements = sum(product_list[i] for i in range(0, len(product_list), 10))

    return sum_tenth_elements

if __name__ == '__main__':
    data = utils.read_data_from_file('alg_lab3/task6/textf/input.txt')
    arr_a = data[1]  # Первый массив
    arr_b = data[2]  # Второй массив
    result = sum_of_every_tenth_product(arr_a, arr_b)
    utils.write_data_to_file('alg_lab3/task6/textf/output.txt', [result])
    print(result) 

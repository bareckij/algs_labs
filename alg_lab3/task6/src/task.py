from alg_lab3.task1.src.task1 import randomized_quick_sort 

def sum_of_every_tenth_product(array_a, array_b):
    product_list = []
    for b in array_b:
        for a in array_a:
            product_list.append(a * b)
    
    randomized_quick_sort(product_list, 0, len(product_list) - 1)
    sum_tenth_elements = sum(product_list[i] for i in range(0, len(product_list), 10))

    return sum_tenth_elements

if __name__ == '__main__':
    result = sum_of_every_tenth_product()
    print(result)  # Вывод результата, если нужно

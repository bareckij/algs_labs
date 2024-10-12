def add_two_binary(first_number, second_number):
    n = max(len(first_number), len(second_number))

    first_number = [0] * (n - len(first_number)) + first_number
    second_number = [0] * (n - len(second_number)) + second_number

    result = [0] * (n+1)
    carry = 0
    for i in range(n-1, -1, -1):
        temp_sum = first_number[i] + second_number[i] + carry
        result[i+1] = temp_sum % 2
        carry = temp_sum // 2
    result[0] = carry
    return result

print(add_two_binary([1, 1, 1, 0], [1, 1, 1]))
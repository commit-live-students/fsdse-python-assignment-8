
def get_even_numbers(input_num):
    if input_num <= 0:
        raise ValueError("number must be greater than 0")
    result = []
    for i in range(1, input_num + 1):
        if i%2 == 0:
            result.append(i)
    return result

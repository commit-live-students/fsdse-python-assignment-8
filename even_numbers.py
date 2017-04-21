def get_even_numbers(n):
    if n < 0:
        raise ValueError('Number should be greater than 0')
    numbers = []
    for num in range(1, n):
        if num % 2 == 0:
            numbers.append(num)

    return numbers

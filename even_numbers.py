def get_even_numbers(n):
    if type(n) != int or n < 1:
        print('Enter a positive integer')
        return 1

    even_numbers = [x for x in range(2, n) if x % 2 == 0]
    return even_numbers

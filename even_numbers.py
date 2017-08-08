def get_even_numbers(number):
    evens = []
    count = 2
    while count <= number:
        if count % 2 == 0:
            evens.append(count)
            count = count + 1
        else:
            count = count + 1
    return evens

no = 12
print get_even_numbers(no)

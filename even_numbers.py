def get_even_numbers(n):
    i = 1
    d = []
    while i <= n:
        if i%2 == 0:
            d.append(i)
        i += 1
    return d

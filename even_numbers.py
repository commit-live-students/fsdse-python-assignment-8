def get_even_numbers(n):
    even_list = []
    for x in range (1,n+1):
        if n > 0:
            if x % 2  == 0:
                even_list.append(x)
    return even_list


print get_even_numbers(10)

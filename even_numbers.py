def get_even_numbers(n):
    even = []
    if n>0:
        for i in range(1,n+1):
            if i % 2 == 0:
                even.append(i)
    #print(even)
    return even
get_even_numbers(10)

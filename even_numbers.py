def get_even_numbers(n):
    l = []
    for i in range(2,n+1,2):
        if i % 2 == 0 :
            l.append(i)
    return l
print get_even_numbers(n=12)

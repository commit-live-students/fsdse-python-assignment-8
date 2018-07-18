def get_even_numbers(n):
    l=[]
    for k in range(1,n+1):
        if (k%2==0):
            l.append(k)
    return l
print get_even_numbers(9)

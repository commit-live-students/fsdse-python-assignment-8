def get_even_numbers(n):
    if n < 0 or not isinstance(n,int):
        return
    return [d for d in range(1,n+1) if d%2==0]

#print(get_even_numbers(2))

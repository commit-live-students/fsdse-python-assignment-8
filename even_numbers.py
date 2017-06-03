def get_even_numbers(n):
    if n < 0 or not isinstance(n,int):
        return
    return [s for s in range(1,n+1) if s%2==0]

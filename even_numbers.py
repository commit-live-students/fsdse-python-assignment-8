def get_even_numbers(n):
    if n<=2:
        return "Not an even number"
    else:
        even=list(range(2,n,2))
    return even

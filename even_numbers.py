def get_even_numbers(num):
    l1 = []
    if num > 0:
        l1 = [x for x in range (2,num+1) if x%2==0]

    return l1    

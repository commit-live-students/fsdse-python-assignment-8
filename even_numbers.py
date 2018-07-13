l = []

def get_even_numbers(n):
    if n  <= 0:
        print "Number should not be 0"
    for x in range(1,n):
        if(x%2 == 0):
            l.append(x)
    return l

print get_even_numbers

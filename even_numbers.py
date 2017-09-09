def get_even_numbers (n):
    evens = []
    if (n<0):
        print "Pass a number more than or equal to 0"
    else:
        for i in range (1,n):
            if i%2 == 0:
                evens.append(i)

    return evens

if __name__ == "__main__":
    print get_even_numbers (-1)
    print get_even_numbers (0)
    print get_even_numbers (1)
    print get_even_numbers (12)

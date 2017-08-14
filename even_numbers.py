def get_even_numbers(n):

    evens = []

    if n / 2 > 0:

        for i in range (2,n):

            if i % 2 == 0:
                evens.append(i)
        return evens

    else:
        return 'Please Enter Positive Number'



'''
a = get_even_numbers(-20)
print a
'''

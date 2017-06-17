even=[]
def get_even_numbers(n):
    if n<=1:
        print "Number is less than 1"
    else:
        if n>1:
            for i in range (1,n):
                if i%2==0:
                    even.append(i)
    return even

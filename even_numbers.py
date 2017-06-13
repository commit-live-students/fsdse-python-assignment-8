def get_even_numbers(n):
    a=[]
    i=2
    if n>0:
        while(i<n):
            if(i%2==0):
                a.append(i)
            i=i+1
    return a

print get_even_numbers(20)

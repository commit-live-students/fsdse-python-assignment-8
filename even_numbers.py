n=10
l=[]
def get_even_numbers(n):
    for k in range(1,n+1):
        if k%2 == 0:
            #print k
            l.append(k)
    return l
if n>0:
    a=get_even_numbers(n)
    print a

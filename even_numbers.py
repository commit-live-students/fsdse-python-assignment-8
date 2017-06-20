# Get all even numbers starting from 1

def get_even_numbers(n):
    even_list = []
    for i in range(1, n+1):
        if (i%2 == 0):
            even_list.append(i)
        else: continue
    print ("Even List: ", even_list)
    return even_list

get_even_numbers(10)

#DOne, Not Posted =================================================================================

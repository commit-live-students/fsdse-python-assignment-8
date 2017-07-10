def get_even_numbers(last_Digit):

    Even_Number = []
    if last_Digit > 0 :
        for i in range(1,last_Digit) :
            if i%2==0 :
                Even_Number.append(i)
    else :
        print "Please enter any value above zero!"
    return Even_Number

get_even_numbers(12)

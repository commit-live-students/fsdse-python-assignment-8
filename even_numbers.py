def get_even_numbers(last_Digit):

    List_of_Even_Number = []
    if last_Digit > 0 :
        for i in range(1,last_Digit) :
            if i%2==0 :
                List_of_Even_Number.append(i)
    else :
        print "Please enter any value above zero!"
    return List_of_Even_Number

get_even_numbers(12)

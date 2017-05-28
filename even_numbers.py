def get_even_numbers(number):
    evenList = []
    for i in range (1,number+1):
         if number > 0:
             if i%2 == 0:
                 evenList.append(i)
    return evenList

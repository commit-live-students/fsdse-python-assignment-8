def get_even_numbers(num):
    ls = []
    if num > 0:
        for x in range(1,num):
            if (x%2==0):
                ls.append(x)
        return ls
    elif num < 0:
        print("number is less than zero")

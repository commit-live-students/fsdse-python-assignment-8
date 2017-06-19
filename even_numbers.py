def get_even_numbers(num):
    EmptyList = [ ]
    if num > 0:
        for i in range (1, 20):
            if i % 2 == 0:
                EmptyList.append(i)

        return EmptyList 

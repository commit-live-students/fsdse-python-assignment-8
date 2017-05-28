def get_even_numbers(num=10):
    even = []
    if num < 1:
        print("Enter number greater than 1")
    else:
        for i in range(1, num):
            if i % 2 == 0:
                even.append(i)

        return even

print get_even_numbers(10)

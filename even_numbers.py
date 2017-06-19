def get_even_numbers(number):
    numbers = range(number)
    even_numbers = numbers[2:number:2]
    return even_numbers

number = 21
get_even_numbers(number)

def get_even_numbers(n):
    ls =[]
    for i in range(1,n):
        if i%2 == 0:
            ls.append(i)
    return ls

tmpl = get_even_numbers(20)
print tmpl

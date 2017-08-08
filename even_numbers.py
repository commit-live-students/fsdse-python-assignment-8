def get_even_numbers(x):
	lst = []
	while x > 0:
		if x%2 == 0:
			lst.append(x)
		x-= 1
		lst.sort()
	return lst

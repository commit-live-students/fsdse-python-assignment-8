def get_even_numbers(n):
	p = []
	[p.append(i) for i in range(1,n) if(i%2 == 0)]
	return p

print get_even_numbers(12)

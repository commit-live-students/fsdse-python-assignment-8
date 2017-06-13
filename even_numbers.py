lis=[]

def get_even_numbers(num):
	if(num>0):
		for num in range(1,num):
			if(num%2==0):
				lis.append(num)
		return lis


get_even_numbers(10)

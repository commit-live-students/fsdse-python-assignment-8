def get_even_numbers(n):
   if n<0: return "Please enter a number greater than 0"

   L = [i for i in range(1,n+1) if (i%2)==0]
   return L


print get_even_numbers(10)

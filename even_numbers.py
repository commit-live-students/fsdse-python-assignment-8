def get_even_numbers(n):
        a = []
        if n > 0:
            for i in range(1,n):
                if(i%2 == 0):
                    a.append(i)
            return a
        else:
            print "Number should not be less than 0"

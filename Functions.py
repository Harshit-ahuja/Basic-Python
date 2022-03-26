def sum(a,b) :
    '''This function finds the sum of 2 numbers''' # This is doc string
    c = a + b
    print(c) # 8
    print(sum.__doc__)
    return c

print(sum(4, 4)) # 8
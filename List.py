l1 = [1, 2, 3, 4]
l2 = [5, 'hello', 4.44]

print(l1, l2)

l3 = [1, 5, 7, 9]
l4 = [1, 5, 7, 9]
l5 = [1, 7, 9, 5]

print(l3 == l4) # True
print(l3 == l5) # False

lx = [2, 9, 5, 8]
lx.append('harsh')
lx.insert(0, 'hello')
lx.remove(5)
print(lx)

print(lx.pop())
print(lx)

# lx.remove(1) # Error
# print(lx)



# List Comprehension 
ly = [x**2 for x in range(0, 6)]
print(ly) # [0, 1, 4, 9, 16, 25]




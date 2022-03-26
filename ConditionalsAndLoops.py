# Conditionals <--------------------------------->

a = int(input())

if(a > 10) :
    if(a > 20) :    # This is nested 'if' in python
        print("Number is greater than 20")
    else :
        print("Number is greater than 10 but less than  20")
elif(a == 10) :
    print("Number is equal to 10")
else :
    print("Number is not greater than 10")


# Loops <-------------------------------------->


# Simple for loop
for i in range(0, 10) :
    print(i)

# Using 'for' loop for list traversal 
li = ['best', 'hello', 'harsh'] # A Python List
for i in li :
    print(i)

# Nested For Loop
for i in range(0, 3) :
    for j in range(0, 2) :
        print(i, j)


# Simple While Loop
count = 0
while(count < 3):
    print("Harsh")
    count = count + 1

# Using Break Statement in 'for' loop ('break' immediately terminates the loop)
name = 'Harsh'
for i in name :
    print(i)
    if(i == 'r') :
        break

print("Outside For Loop")

# Using Pass Statement in 'for' loop ('pass' represents an empty block of code)
surName = "Ahuja"
for i in surName :
    pass

print("Outside For Loop")

# Using Continue Statement in 'for' loop ('continue' omits the code written below it and simply passes the control back to the loop)
anotherName = "Payushi"
for i in anotherName :
    if(i == 'y') :
        continue
        print("y character found")

print("Outside For Loop")


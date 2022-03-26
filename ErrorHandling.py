# x = 5 / 0  # ZeroDivisionError
# print(x) 


# Exception Handling using 'try' and 'except'
try :
    x = 5 / 0
    print(x)
except :
    print("Error Occured")


# Multiple 'except' statement ('except' statement can also target a particular error)
try :
    print(z)
    x = 6 / 0
except NameError:
    print("Variable Not defined")
except ZeroDivisionError :
    print("Divison by Zero is invalid")


# 'try' , 'except' and 'else' (When 'try' block executes well, then 'except' block does not executes, instead 'else' block executes)
def func(a, b) :
    try :
        c = (a + b) / (a - b)
    except ZeroDivisionError :
        print("Divion by Zero is Invalid")
    else :
        print(c)

func(5, 2)
func(5, 5)


# 'finally' block 
# 'finally' block always gets executed irrespective of whether 'try' executes well or not, whether 'except' block gets executed or not, whether 'else' block gets executed or not

def func(a, b) :
    try :
        c = (a + b) / (a - b)
    except ZeroDivisionError :
        print("Divion by Zero is Invalid")
    else :
        print(c)
    finally :
        print("This block will always execute")

func(5, 2)
func(5, 5)



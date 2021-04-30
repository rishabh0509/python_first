var = 9 #global variable
loop = True

def func(x):
    newVar = 7 #local variable to the function func()
    global var #changing global variable to local
    var = 19
    if x == 5:
        return newVar

def otherFunc():
    newVar = 5
    print(newVar)

func(2)
print(var)

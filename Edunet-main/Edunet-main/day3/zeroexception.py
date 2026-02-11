def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
       print("error:division by zero error")

print(add(5,6))
print(sub(5,6))
print(mul(5,6))
print(div(10,0)) # here in o/p we get none bcz we used print two times 
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divison(a,b):
    if b==0:
        raise ValueError("cannot divide by 0")
    return a/b

if __name__=="__main__":
    print("add result is",add(23,4))
    print("substract result is",substract(34,12))
    print("multiply result is",multiply(3,9))
    print("division result is",divison(60,12))
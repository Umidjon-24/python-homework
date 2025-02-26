def check(func):
    def wrapper(*args):
        print("Before")
        result = func(*args)
        print("After")
        return result
    return wrapper

@check
def div(a,b):
    try:
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("Can not divide by zero")

div(6,1)
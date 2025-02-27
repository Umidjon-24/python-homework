def check(func):
    def wrapper(*args):
        try:
            result = func(*args)
            print(result)
            return
        except ZeroDivisionError:
            print("Can not divide by zero")
            return
    return wrapper

@check
def div(a,b):
    return a/b

div(6,2)
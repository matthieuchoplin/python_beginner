def my_decorator(function):
    print("Decorator called with in parameter the function", function)
    return function

@my_decorator
def hello():
    print("Hello!")

hello()
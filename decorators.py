def greet(fx):
    def modified_func():
        print("hello good morning all!!!")
        fx()
    return modified_func

@greet
def hello():
    print("Ram")

hello()

'''
decorator will modify the function given below and return the modified function

'''

def greet_math(func):
    def math_func(*args):
        print("Welcome to math lecture!!")
        func(*args)
    return math_func
        

@greet_math
def add(a,b):
    print(a+b)

@greet_math
def sub(a,b):
    print(a-b)

add(2,3)
sub(7,5)

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



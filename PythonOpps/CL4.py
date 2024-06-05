#DECORATORS....................................
# def greet(fx):
#     def mfx():
#         print("GOOD Morning")
#         fx()
#         print("Thanks For Visiting Us")
#     return mfx
# @greet
# def hello():
#     print("Hello World")

# hello()
# greet(hello)()


# def great(fx):
#     def info(*args, **kwargs):  
#         print("very good morning")
#         fx(*args, **kwargs)
#         print("thank you")
#     return info
# # @great
# def add(a,b):
#     print(a+b)

# # add(1,3)
# great(add)(1,6)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
my_function(7,8)
# Unpacking Tuples with *args

# This time I've defined a function for you. It's called count_sevens ,and you need to call it twice.

# First, call it with the arguments 1,4, and 7 and save the result to a variable called result1.
# Next, call the same count_sevens function, passing in all the numbers contained in the nums list as
# individual arguments (unpack the list).  Save the result to a variable called result2 .

# NO TOUCHING! =================================================================
import inspect
from functools import partial


def count_sevens(*args):
    # it is of type tuple which it unpacks if the function call argument is appended with *
    print(args)
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34, 45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17,
        11, 7, 11, 8, 4, 6, 2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1, 4, 7)

result2 = count_sevens(*nums)

print("result1: ", result1)
print("result2: ", result2)

# Dictionary unpacking with **kargs

# Oh boy, this is a complicated set of instructions.  Bear with me.
# Write a function called calculate that accepts a list of keyword arguments
# make_float , a boolean which returns a float if True or an integer if False.
# operation which is either 'add', 'subtract', 'multiply', and 'divide'.

# first which is a number, second , which is another number, and message which is a string that can be added.
# The function should return the result of actually running the specified operation with the first and second keyword arguments.
# The result of the operation with the first  and second  is an integer if the make_float  keyword argument is False ,
#  otherwise the result of the operation is a float. If a message is specified, it should return the message keyword argument + the result of the operation.  Otherwise, it should return the string  "The result is " joined with the result of the operation.
# See the code examples for some more information.

'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kargs):
    print(kargs.get("operation"))
    result = None
    if kargs.get("operation") == "add":
        result = kargs.get("first") + kargs.get("second")
    elif kargs.get("operation") == "divide":
        result = kargs.get("first") / kargs.get("second")

    if kargs.get("make_float") is True:
        result = float(result)
    else:
        result = int(result)

    if kargs.get("message"):
        msg = kargs.get("message")
        return f"{msg}  {result}"
    else:
        return f"The result is : {result}"


input_a = {"make_float": False, "operation": 'add',
           "message": 'You just added', "first": 2, "second": 4}
result_a = calculate(**input_a)
result_b = calculate(make_float=True, operation='divide', first=3.5, second=5)
print(result_a)
print(result_b)


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final


# Partial Function :- Partial functions allows us to fix certain number of args of function and
# generate a new function

def addition(a, b, c):
    return 100 * a + b * 10 + c


# here 2 args of functions are fixed - very handy when dealing and using 3rd party libraries and functions
addition_partial = partial(addition, c=5, b=2)
# where if we wan to tweak in the args of existing functions and deriving our own partial functions out of it
print(addition_partial(3))


# Edit the function provided by calling partial() and replacing the first three variables in func().
# Then print with the new partial function using only one input variable so that the output equals 60.
# Following is the exercise, function provided:


def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x


# Enter your code here to create and print with your partial function
mul_partial = partial(func, 5, 6, 7)
print(mul_partial(60))

# Dunder Methods:
# _name - declaring private variables in class
# __name -- leads to name mangling - attribute error since it's used under the hood it associates it with
# particular class to avoid confusion/name conflicts when Inheritance is implemneted
# __name__ - python specific methods like __init__, __len__ etc

# Closures
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.


def transmit_to_space(message, num):
    print("This is the enclosing function")

    def data_transmitter():
        print("The nested function")
        num = 5
        print(message, num)
        return (message, num)
    print(num)
    return data_transmitter()


print(transmit_to_space("Test message", 10))


def print_msg(number):
    def printer():
        print("Here we are using the nonlocal keyword")
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)


print_msg(9)


def greet():
    # variable defined outside the inner function
    name = "John"

    # return a nested anonymous function
    return lambda: "Hi " + name


# call the outer function
message = greet()

# call the inner function
print(message())

# Output: Hi John

print(inspect.getmembers(greet()))

# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

# outer function
def multiplier_of(n):
    # inner function
    def multiplier(number):
        return number * n

    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

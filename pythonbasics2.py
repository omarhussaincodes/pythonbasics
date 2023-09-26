#  Iterators and Generators
# Here name is iterable and not iterator
# The next() calls on iterator and returns iteraotor
# "Hello" -- Iterable
# iter("hello") --- Iterator returns iterator

import pickle
import json
name = "Larry"
# next(name) # error str object not an iterator
print(iter(name))
iterator_obj = iter(name)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
# StopIteration since iteration is complete
# print(next(iterator_obj))


def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            it = next(iterator)
            print(it)
        except StopIteration:
            print("END")
            break


my_for_loop([5, 2, 3])

# Write a function called week, which returns a generator that yields each day of the week,
# starting with Monday and ending with Sunday.
# After Sunday, the generator is exhausted.  It does not start over.

'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


def week():
    for day in days:
        yield day


print(week())
day_gen = week()  # return generator object

print(next(day_gen))
print(next(day_gen))
print(next(day_gen))
print(next(day_gen))
print(next(day_gen))
print(next(day_gen))
print(next(day_gen))

# yes_or_no
# Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.
'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''


def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        # ternary operator python
        # answer = 'no' if answer == 'yes' else 'yes'
        if answer == 'yes':
            answer = 'no'
        else:
            answer = 'yes'


print(yes_or_no())

gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#  let's say we need to create a list of integers which specify the
#  length of each word in a certain sentence, but only if the word is not the word "the".


def sentence_len(sentence):
    sen_list = sentence.split()
    result = []
    for word in sen_list:
        if (isinstance(word, str) and word != "the"):
            result.append(
                {
                    "word": word,
                    "l": len(word)
                })

    return result


sentence = "the quick brown fox jumps over the lazy dog"
print("result1: ", sentence_len(sentence))

# same above solution with list comprehension


def sentence_len_list_comp(sentence):
    sen_list = sentence.split()
    result = [{"word": word, "l": len(word)}
              for word in sen_list if word != "the" and isinstance(word, str)]

    return result


print("result2: ", sentence_len_list_comp(sentence))

# Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [num for num in numbers if num > 0]
print(newlist)


# Lambda Functions - Anonymous functions - No name - Inline functions

def sum(x, y): return x+y


print(sum(1, 2))

# Write a program using
# lambda functions to check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.

l = [2, 4, 7, 3, 14, 19]
for i in l:
    # your code here
    def isOdd(x): return (x % 2) == 1
    print(isOdd(i))

# Multiple function arguments


def foo(first, second, third, *args):
    print(first)
    print(second)
    print(third)
    print(list(args))


foo(1, 2, 3, 4, 5, 6, 7, 8, 9)

# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter


def math_op(first, second, third, **kargs):
    if kargs.get("action") == 'sum':
        sum = first + second + third
        print(f"The sum of given numbers is: {sum}")
        return sum
    if kargs.get("action") == 'product':
        product = first * second * third
        print(f"The product of given numbers is: {product}")
        return product


result = math_op(4, 6, 7, action="product")
print("Result: ", result)

# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received. The bar must return True
# if the argument with the keyword magicnumber is worth 7, and False otherwise.

# edit the functions prototype and implementation


def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kargs):
    if int(kargs.get("magicnumber")) == 7:
        return True
    else:
        return False


print("=================")
# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

# Exception Handling

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!


def get_last_name():
    try:
        return actor["last_name"]
    except:
        return actor["name"].split()[1]


# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

# Sets
a = set(["Jake", "John", "Eric"])
print(a)
b = {"John", "Jill"}
print(b)

print(type(a), type(b))

# Set Union
print(a.union(b))

# Intersection
# To find out which members attended both events, you may use the "intersection" method:
print(a.intersection(b))

# To find out which members attended only one of the events, use the "symmetric_difference" method:
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To find out which members attended only one event and not the other, use the "difference" method:
print(a.difference(b))
print(b.difference(a))

# Serialization

# To load JSON back to a data structure, use the "loads" method.
# This method takes a string and turns it back into the json object datastructure:


json_string = ""
# arg will be json string which will be converted to json object data structure
try:
    print(json.loads(json_string))
except:
    print("Json encoding failed")

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:

try:
    json_string1 = json.dumps([1, 2, 3, "a", "b", "c"])
    print(json_string1)
except:
    print("Json Decoding failed!")


# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# The aim of this exercise is to print out the JSON string with key-value pair "Me" : 800 added to it.

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it


def add_employee(salaries_json, name, salary):
    # Add your code here
    json_obj = json.loads(salaries_json) # converts to json obj datastructure
    json_obj[name] = salary # adding new entry to the ds

    return json.dumps(json_obj) # converting back to json string


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

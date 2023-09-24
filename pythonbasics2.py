#  Iterators and Generators
# Here name is iterable and not iterator
# The next() calls on iterator and returns iteraotor
# "Hello" -- Iterable
# iter("hello") --- Iterator returns iterator

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
        answer = 'no' if answer == 'yes' else 'yes'


print(yes_or_no())

gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
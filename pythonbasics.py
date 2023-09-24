print("hey"*10)
print([1, 2, 3] * 4)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = (list(x_list) + list(y_list)) * 10

print(x_list)
print(y_list)
print(big_list)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
firstname = "omar"
lastname = "beckham"
print("Hi my name is %s %s" % (firstname, lastname))

# You will need to write a format string which prints out the data using the following syntax:
#  Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)  # tuple
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

astring = "Hellohworld!"
print(astring[3:7])
print(astring[3:7:2])
# reverse a string
print(astring[::-1])

# Fix the CODE
s = "Str thera! whatome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The characters with even index are '%s'" % s[::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# Change the variables in the first section, so that each if statement resolves as True.
# change this code
number = 19
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# For loops
print("Loops")
for x in range(5):
    print(x)

for z in range(1, 11):
    print(z)

for a in range(2, 11, 2):
    print(a)

# while loops  with else statment
count = 1
while (count < 4):
    print(count)
    count += 1
else:
    print("Count reached %d" % count)

# while loops with break and else statment
counter = 0
while True:
    counter += 1
    if counter > 5:
        print(counter)
        break
    else:
        print(
            "Else will not be printed if break statment is executed as it breaks the loop.")

for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Loop through and print out all even numbers from the numbers list in the same order they are received.
# Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for num in numbers:
    if num % 2 == 0 and num < 237:
        print(num)

for number in numbers:

    if number % 2 == 0:
        continue

    if number == 237:
        break

    print(number)

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


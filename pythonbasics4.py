# zip function :- The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
names = ['Dean', 'Sophia', 'Fleur']
ages = [51, 20, 20]
hair_color = ['black', 'brown', 'black']

zip_info = zip(names, ages, hair_color)
# t1, t2, t3 = zip_info
# print(t1)
# print(t2)
# print(t3)
tup = tuple(zip_info)
print("tup -----", tup)
lis_t = list(tup)
print("list ----", lis_t)

tuple_to_lists = [list(tup) for tup in lis_t]
print("tuple_to_lists --- ", tuple_to_lists)

# Multiple Assignment in python similar to destructing in JS

names = ["Dean", "Fleur", "Lia", "Sophie"]
ages = [52, 51, 19, 20]
hair_color = ['black', 'brown', 'blonde', 'green']
zipped_info = zip(names, ages, hair_color)
print(zipped_info)
dean, fleur, lia, sophie = zipped_info
print("The dean variable holds:", dean)
print("The fleur variable holds:", fleur)
print("The lia variable holds:", lia)
print("The sophie variable holds:", sophie)

# Pyhtonista Swap

x = "elon"
y = "twitter"
x, y = y, x
print(f"x is now {x} and y is {y}")

# Dictionaries

# create dictionary:
player_dict = dict({
    'name': 'Beckham',
    'age': 27,
    "hair_color": 'Black',
})
print(player_dict)
print("=====================================================")
ml_dictionary = {
    "Supervised Learning": "A type of machine learning where the model learns from labeled data.",
    "Unsupervised Learning": "A type of machine learning where the model learns from unlabeled data.",
    "Feature Extraction": "The process of selecting relevant features from raw data for use in machine learning.",
    "Gradient Descent": "An optimization algorithm used to minimize the loss function during model training."
}
print(ml_dictionary)

# reading from dictionary:

# reading values with keys
print(ml_dictionary["Supervised Learning"])
try:
    print(ml_dictionary['key_does_not_exists'])  # gives KeyError
except KeyError:
    print("The value for the passed key does not exists!")
term_to_look_for = "Reinforcement Learning"
result = ml_dictionary.get(term_to_look_for, "Term not found!")
print(result)

# update dictionary
term_to_update = "Gradient Descent"  # key to update
new_description = "An iterative optimization algorithm used to minimize the cost function."

if (ml_dictionary.get(term_to_update) != None):
    ml_dictionary[term_to_update] = new_description
    print("Update Successful!!!!")
else:
    print("Cannot update the data which does not exists!")


def display_ml_dict():
    for term, desc in ml_dictionary.items():
        print(f"{term}: {desc}")


# delete dictionary
term_to_delete = "Unsupervised Learning"

if term_to_delete in ml_dictionary:  # if key in dict
    del ml_dictionary[term_to_delete]
    print("Deletion succesful")
else:
    print(f"{term_to_delete} not found in dictionary.")

print("Updated Dictionary!")
display_ml_dict()

print("!!!MAP!!!")
# map function in python:

# map function is a transformation function which accepts first arg as function and second arg as iterable on which mapping needs to be performed.
full_names_list = [
    {"first_name": 'Larry', "last_name": 'Page'},
    {"first_name": 'Elon', "last_name": 'Musk'},
    {"first_name": 'Cal', "last_name": 'Newport'},
]
print(type(full_names_list))
last_names_list = list(
    map(lambda name: f"Last name : {name['last_name']}", full_names_list))
print(last_names_list)

# filter and map together
filtered_data = list(map(lambda n: f"Result:{n['first_name'], n['last_name']}",
                         filter(lambda name: name['last_name'] == 'Musk', full_names_list)))
print(filtered_data)

# Use all datatypes available in python as a variable, assign values to variables and perform valid  operations on them.

# Integer
integer_var = 10

# Float
float_var = 3.14

# String
string_var = "Hello, Python!"

# Boolean
boolean_var = True

# List
list_var = [1, 2, 3, 4, 5]

# Tuple
tuple_var = (6, 7, 8)

# Set
set_var = {2, 4, 6, 8}

# Dictionary
dict_var = {"name": "Alice", "age": 25, "city": "Wonderland"}

# Perform Operations

# Arithmetic Operations
sum_result = integer_var + float_var
difference_result = float_var - integer_var
product_result = integer_var * float_var
division_result = float_var / integer_var

# String Operations
concatenated_string = string_var + " Welcome!"
string_repeated = string_var * 3

# List Operations
list_sum = sum(list_var)
list_length = len(list_var)
list_append = list_var + [6, 7]
list_repeated = list_var * 2

# Tuple Operations
tuple_concatenated = tuple_var + (9, 10)
tuple_repeated = tuple_var * 3

# Set Operations
set_union = set_var.union({10, 12})
set_intersection = set_var.intersection({2, 6})
set_difference = set_var.difference({2, 4})

# Dictionary Operations
dict_keys = dict_var.keys()
dict_values = dict_var.values()
dict_items = dict_var.items()

# Boolean Operations
bool_and = boolean_var and True
bool_or = boolean_var or False
bool_not = not boolean_var

# Output Results
print("Arithmetic Operations:", sum_result, difference_result, product_result, division_result)
print("String Operations:", concatenated_string, string_repeated)
print("List Operations:", list_sum, list_length, list_append, list_repeated)
print("Tuple Operations:", tuple_concatenated, tuple_repeated)
print("Set Operations:", set_union, set_intersection, set_difference)
print("Dictionary Operations:", dict_keys, dict_values, dict_items)
print("Boolean Operations:", bool_and, bool_or, bool_not)

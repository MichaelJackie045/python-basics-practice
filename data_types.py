# Assigning data types to variables
integer_var = 10                        # Integer
float_var = 10.5                        # Float
string_var = "Hello, Python!"           # String
bool_var = True                         # Boolean
list_var = [1, 2, 3, 4, 5]              # List
dict_var = {"name": "John", "age": 30}  # Dictionary

# String operations
uppercase_string = string_var.upper()                # Convert to uppercase
concatenated_string = string_var + " How are you?"   # Concatenate strings

# List operations
list_length = len(list_var)   # Get the length of the list
list_sum = sum(list_var)      # Sum of list elements
list_var.append(6)            # Add an element to the list

# Dictionary operations
dict_keys = dict_var.keys()      # Get dictionary keys
dict_values = dict_var.values()  # Get dictionary values
dict_var["city"] = "New York"    # Add a new key-value pair

# Arithmetic operations
sum_result = integer_var + float_var # addition
diff_result =integer_var - 5 # subtraction
mult_result = integer_var * 2 # multiplication
div_result = integer_var / 2 # division
mod_result = integer_var % 3 # modulus
exp_result = integer_var ** 2 # exponentiation

# comparison operations
is_equal = integer_var == float_var # equality
is_not_equal = integer_var != 5 # inequality
is_greater = float_var > 20 # greater than
is_less = integer_var < 5 # less than

# logical operations
and_result = bool_var and (integer_var > 5) # logical AND
or_result = bool_var or (integer_var < 5)   # logical OR
not_result = not bool_var                     # logical NOT

print(uppercase_string)
print(concatenated_string)
print(list_length)
print(list_sum)
print(list_var)
print(dict_keys)
print(dict_values)
print(dict_var)

print(sum_result)
print(diff_result)
print(mult_result)
print(div_result)
print(mod_result)
print(exp_result)
print(is_equal)
print(is_greater)
print(is_not_equal)
print(and_result)
print(or_result)
print(not_result)
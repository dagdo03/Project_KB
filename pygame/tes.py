string_value = "variable"
number_value = 42

# Combine string and number to create variable name
variable_name = string_value + str(number_value)

# Assign a value to the dynamically created variable
globals()[variable_name] = "Hello, World!"

# Access the dynamically created variable
print(variable_name)  # Output: variable42
print(variable42)     # Output: Hello, World!
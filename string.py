# Print string variable
string_name = "Python"
print(string_name)


# String concatenation using "+" 
# Example 1
print("Hello and welcome to " + string_name + " world" )


# Example 2
first_name = "Jennifer"
last_name = "Aniston"
print(first_name + " " + last_name)

# Newline
print(first_name +"\n"+ last_name)

# Escape character
print(first_name +"\""+ last_name)

# Using string function
print(first_name.upper() + " " + last_name.lower())

# Validate string is upper or lower, returns true or false value
print(first_name.isupper())
print(last_name.islower())
print(first_name.upper().isupper())

# Length of string
print(len(first_name))

# Get individual character inside a string. String index starts with zero
print(first_name[0])

# Return index of a character inside a string
print(first_name.index("e"))

# Replace function
print(first_name.replace(first_name,"Anna"))
print(first_name)


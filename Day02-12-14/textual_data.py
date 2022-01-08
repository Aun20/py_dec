# Data Types (Strings, Integers, Boolean)
# Numeric - Int, Float & Complex no.
# Textual Data (Strings) --> Anything between single/double quotes is textual data called Strings
# Anything between triple single/double quotes is a sentence
# variable --> Helps us to store data. e.g : greeting = "hello"

'''
In computer science, a data structure is a data organization, management, and storage format
that enables efficient access and modification
'''

greeting = "Hello" # variable called "greeting" is holding a string data type
name = 'John'

#message = greeting + ',' + name # + concatenate two variables
#message = "{}, {}".format(greeting,name) # this was used in old py version. Its called .(dot) format method
message = f"{greeting}, {name}" # this is called f-string method.

print(message)


print(greeting) # acessing the variable
# python runs line by line and stops as soon as it gets an error

#print(Greeting) - it will give an error
# python is case sensitive
# string should start with quotes and end with quotes

'''
Numbers:
Whole Numbers - Integers (Int)
Decimals - Floats (float)
'''

num = 3.4

#print(type(num))

# + - addition
# - - subtraction
# * - multiplicaiton
# / - division
# // - floor division
# ** - exponent
# % - modulus

print(15*5)

num = 1

#num = num+1 # increment operator
num+= 2

print(num)

# Comparison operator

# == - equal to 
# != - not equal to
# > - greater than
# < - less than
# >= - greater than equal to
# <= - less than equal to
# True or False are called Boolean

num_1 = 1
num_2 = 5

print(num_1 > num_2)

num_1 = '100' # string value
num_2 = '400'

num_1 = int(num_1) # both have to be converted to integer or else it will give an error.
num_2 = int(num_2)

print(num_1+num_2)

print(round(3.75))


# Brittnay Squires
# UWYO COSC 1010
# February 11, 2024
# Lab 02 
# 40: 
# Sources, people worked with, help given to: Soudabeh Bolouri, Ryan Zafft
# your
# comments
# here

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010")  

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, COSC1010"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
cowboy_message = "cowboy joe"
print(cowboy_message.title())

# Using f-strings and variables print out the solved solution for y = mx+b where:
# x = 2
# m = 1 
# b = 13 

m = 1
x = 2
b = 13

variables = f"m = {m}, x = {x}, b = {b}"

y = ((m)*(x))+(b)
print(y)


# Your print message should be of the form "Given the variables m,x b we have y=m*x+b"
# Where  the variables are replaced with their values in the string

mxb_message = "Given the variables m,x b we have"

print((mxb_message), (variables))
print("y=",(m),"*",(x),"+",(b))


# This one is more advanced then the others and will involve several steps 
# Start by declaring the following variables:
# x = 5
# y = 7
# z = 9 

x = 5
y = 7
z = 9

# print the sum of x,y,z

print(x+y+x)

# Print the sum of y raised to the z with the result multiplied by x

print((y**z)*x)

# Print the result of raising z to the sum of x and y 

print(z**(x+y))
# Finally create two strings "Cowboy " and "Joe" (spacing in cowboy intentional)
first_name = "Cowboy "
last_name = "Joe"
print((first_name),(last_name))

# What happens if you add these two string together, assign it to a third variable, and print it

full_name = f"{first_name}{last_name}"
print(full_name)

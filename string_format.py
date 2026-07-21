"""Practice script for Python string formatting."""
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")

name = "Manoj"
age =35
print("My name is {} and I am {} years old".format(name, age))

name = "Ram"
age =20
# % Operator
# %s: This is a placeholder for a string.
# %d: This is a placeholder for an integer.
print("My name is %s and I am %d years old." %(name,age))

# F-strings are also able to evaluate expressions inside the curly braces,
# which can be very handy. For example:
X=10
Y=20
print(f"The sum of x:{X} and y:{Y} is {X+Y}")

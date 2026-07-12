regular_string = "file.txt"
print("Regular String:", regular_string)

regular_string = "C:\\Manoj\\Python\\python-code\\file.txt"
print("Regular String:", regular_string)

#the below code does not work
#regular_string = "C:\Manoj\Python\python-code\file.txt"
#print("Regular String:", regular_string)

# the below is alternative
regular_string = r"C:\Manoj\Python\python-code\file.txt"
print("Regular String:", regular_string)

name = "Man\"oj\""
print(name)

if('a' == 'A'):
    print("equals")
else:
    print("not equal")
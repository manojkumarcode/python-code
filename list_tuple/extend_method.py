#The extend() method is used to add multiple elements to a list. 
# It takes an iterable (such as another list, tuple, or string)
#  and appends each element of the iterable to the original list.

fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits)
print("fruit after extend", fruits)
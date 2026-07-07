#The count() method is used to count the number of occurrences of a specific element in a list in Python.
my_list = [1,2,3,4,5]
count = my_list.count(2)
print("count" , count)

my_list.extend([2,3,3,2,4,5,2,3,3,3,2,2,2,6,1,1,0,0,5,5,6])
count = my_list.count(2)
print("count" , count)
count = my_list.count(3)
print("count" , count)
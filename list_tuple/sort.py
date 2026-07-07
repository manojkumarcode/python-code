#The sort() method is used to sort the elements of a list in ascending order. 
# If you want to sort the list in descending order,
#  you can pass the 'reverse=True' argument to the sort() method.

from test_data import test_list
test_list.sort()
print("after sort:", test_list)
test_list.sort(reverse=True)
print("after sort(reverse=True):", test_list)

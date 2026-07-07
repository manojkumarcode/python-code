#To remove an element from a list. The remove() method removes the first occurrence of the specified value.
from test_data import test_list

print("Original test_list", test_list)
test_list.remove(20)
print("After removal of 20, test_list", test_list)
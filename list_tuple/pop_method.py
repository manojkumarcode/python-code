# pop method is another way to remove the item from list

from del_method import my_list
print("before pop my_list:" , my_list)
removed_element = my_list.pop(1) # Removes and returns the element at index 1
print("removed_element:", removed_element)
print("my list after removal my_list:", my_list)
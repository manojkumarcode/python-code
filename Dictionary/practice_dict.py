
from dict_data import release_year_dict
from dict_data import my_dict

print(my_dict)
print("my_dict.keys()" , my_dict.keys())
print(my_dict.values())

print(my_dict["key1"])

# Access to the value by the key
print(my_dict[(0,1)])

print(release_year_dict)
print(release_year_dict['Thriller'])

print("release_year_dict.keys():",release_year_dict.keys())
del(release_year_dict["Thriller"])
print("after release_year_dict.del():",release_year_dict.keys())

print("list of keys():",list(release_year_dict.keys()))
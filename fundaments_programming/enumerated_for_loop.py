from list_tuple.extend_method import fruits

print(fruits)

# An enumerated for loop comes to your rescue. 
# It's like having a personal assistant who not only hands you the item 
# but also tells you where to find it.
for index, fruit in enumerate(fruits):
    print(f"At position({index}), I found a {fruit}")
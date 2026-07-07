L = ['Michael Jackson', 10.1, 1982]
print("List:", L)

tuple = ('Michael Jackson', 10.1, 1982)
print("tuple", tuple)

#List are mutable
L[2] = 1983
print("List:", L)

print(" L[-2]:", L[-2])

# Tuple are immutable 
#tuple[2] = 1983
#print("tuple:", tuple)
#TypeError: 'tuple' object does not support item assignment


L = L + ["pop", 10]
print("L after concatenation", L)

print("List also supprot slicing", L[2:5])
print("reverse the List:", L[::-1])

L.extend(["push", "122.28"])

print("reverse the List after L.extend():", L[::-1])

L.append("append1")
print("reverse the List after L.append():", L[::-1])
L.append([2,3.9])
print("reverse the List after L.append():", L[::-1])





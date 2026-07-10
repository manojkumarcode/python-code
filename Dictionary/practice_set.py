set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print("len:", len(set1))
set1.add("manoj")
print("len:", len(set1))

album_list = ["12.2", "Michael", "Pop,rock", "123.45"]
print("album_list", album_list)
album_set = set(album_list)
print("album_set", album_set)

# Verify if the element is in the set
if "Michael" in album_set:
    album_set.remove("Michael")
    print("album_set", album_set)
else:
    print("Michael is not in album_set")

#Remember that with sets you can check the difference between sets, 
# as well as the symmetric difference, intersection, and union:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

intersection = album_set1 & album_set2
print("intersection", intersection)

print(album_set1.difference(album_set2))
print(album_set2.difference(album_set1))

print(album_set2.intersection(album_set1))


#union 

print(album_set1.union(album_set2))

print(album_set1.issuperset(album_set2))

print(album_set1.issubset(album_set2))
print(album_set2.issubset(album_set1))

album_set1.remove("Thriller")
print("After removing Thriller")
print(album_set1.issubset(album_set2))
print(album_set2.issuperset(album_set1))


A = [1,2,2,1]
B = set([1,2,2,1])
print(sum(A), sum(B))
if(sum(A) == sum(B)):
    print ('A and B are equal')
else:
    print ("A and B are not equal")







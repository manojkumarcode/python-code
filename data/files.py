file = open("data/example1.txt", "r")  # filepath and mode
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
print()
file.close()


print("Reading again")
file = open("data/example1.txt", "r")
for line in file:
    print(line, end="")
file.close()


print(f"\n\nReading reading file with \"with\"")

with open("data/example1.txt", "r") as file:
    for line in file:
        print(line, end="")
    print()
    print(file.closed) # once the file in open file.closed with return false

print(file.closed)
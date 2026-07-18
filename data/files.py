fileName = "data/example1.txt"
file = open("data/example1.txt", "r")  # filepath and mode
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
print()
file.close()

print("--- writing to file and readFile.readlines(), w and r mode")

with open("data/example1.txt", "r") as readFile:
    with open("data/example1.txt", "w") as file:
        file.write("This is line1\n")
        file.writelines("This is line3")
    #mytxt = readFile.readlines()
    print(readFile.readlines())

print("----- print(testWritefile.read()) -----")

with open(fileName, 'r') as testWritefile:
    print(testWritefile.read())

print("appending to file, a+ _______________")
with open("data/example1.txt", "a+") as file:
    file.write("\nline6\n")
    file.writelines("line7\n")
    print("before seek(0)")
    print(file.read())
    file.seek(0)
    print("read in a+ mode")
    print(file.read())



print("______Reading again_________")
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

#read all line as list

with open("data/example1.txt", "r") as file: # it automatically closed the file
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    print(lines)
    print(file.name)
    print("using read()")
    test = file.read()
    print(test)

print(lines)

with open("data/example1.txt", "r") as file:
    print("using read()")
    test = file.read()
    print(test)

with open(fileName, 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

